screen rhythm_game():
    default rhythm_game_displayable = RhythmGameDisplayable()
    #add Solid('#000')                                               #adds solid color as background
    image("buttons/back_overlay.png")
    add rhythm_game_displayable

init python:
    class RhythmGameDisplayable(renpy.Displayable):
        def __init__(self):
            super(RhythmGameDisplayable, self).__init__()

            self.has_started = False
            # The first st (timer, st = shown time = seconds)
            # an offset is necessary because there might be delay between when displayable first appears on screen and the time the music starts
            self.time_offset = None

            # Definig offset values

            self.x_offset = 400
            self.track_bar_height = int(config.screen_height * 0.85)
            self.track_bar_width = 12
            self.horizontal_bar_height = 8

            self.note_width = 50
            # Offset the note to the right so it shows at the center of the track
            self.note_xoffset = (self.track_bar_width - self.note_width) / 2

            # The notes are scrolling from top to bottom,  they appear on the track prior to the onset time
            # the scroll time is also the notes' entire lifespan time before it's either hit or miss
            self.note_offset = 3.0 
            #The note now takes 3 seconds to travel the screen, this can be lowered to increase the difficulty of the game
            self.note_speed = config.screen_height / self.note_offset
            # speed = distance / time

            # Number of track bars
            self.num_track_bars = 4
            # Drawing position
            self.track_bar_spacing = (config.screen_width - self.x_offset * 2) / (self.num_track_bars - 1)
            # The xoffset of each track bar
            self.track_xoffsets = {
                track_idx: self.x_offset + track_idx * self.track_bar_spacing
                for track_idx in range(self.num_track_bars)
            }

            # Define the notes onset times
            self.onset_times = [
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0
            ]

            self.num_notes = len(self.onset_times)
            # Assign notes to tracks, same length as self.onset_times
            self.random_track_indices = [
                0,
                1,
                2,
                3,
                0,
                1
            ]

            # Map trand_idx to a list of active note timestamps
            self.active_notes_per_track = {
                track_idx: [] for track_idx in range(self.num_track_bars)
            }

            # Define the drawables
            self.track_bar_drawable = Solid("#fff", xsize=self.track_bar_width, ysize=self.track_bar_height)
            self.horizontal_bar_drawable = Solid("#fff", xsize=config.screen_width, ysize=self.horizontal_bar_height)
            # Map track_idx to the note drawable
            self.note_drawables = {
                0: Image("buttons/left.png"),
                1: Image("buttons/up.png"),
                2: Image("buttons/down.png"),
                3: Image("buttons/right.png")
            }

            # Record all the drawables for self.visit
            self.drawables = [
                self.track_bar_drawable,
                self.horizontal_bar_drawable,
            ]
            self.drawables.extend(list(self.note_drawables.values()))

            # Play music here
            self.has_started = True

        def render(self, width, height, st, at):

            """
            st: a float, the shown timebase, in seconds
            The Shown timebase begins when this displayable is first shown on the screen
            """
            # Cache the first st, when this displayable is first shown on the screen. This allows us to compute the subsequent times when the notes should start falling
            if self.has_started and self.time_offset is None:
                self.time_offset = st

            render = renpy.Render(width, height)

            # Draw the vertical tracks
            for track_idx in range(self.num_track_bars):
                # Look up the offset fro drawing
                x_offset = self.track_xoffsets[track_idx]
                # y = 0 starts from the top
                render.place(self.track_bar_drawable, x=x_offset, y=0)

            # Draw the horizontal bar to indicate where the track ends
            # x = 0 starts from the left

            render.place(self.horizontal_bar_drawable, x=0, y=self.track_bar_height)

            #draw the notes
            if self.has_started:
                #the number of seconds the song has been playing is the difference between the current st and the chached st
                curr_time = st - self.time_offset

                #update self.active_notes_per_track
                self.active_notes_per_track = self.get_active_notes_per_track(curr_time)

                #render the notes on each track
                for track_idx in self.active_notes_per_track:
                    #look up track xoffset
                    x_offset = self.track_xoffsets[track_idx]

                    #loop through active notes
                    for onset, note_timestamp in self.active_notes_per_track[track_idx]:
                        #look up the direction of the arrow on the note image by the track_idx
                        note_drawable = self.note_drawables[track_idx]
                        #compute where on the horizontal and vertical axes the note is
                        note_xoffset = x_offset + self.note_xoffset
                        #the vertical distance from the top that the note has already made is given by time * speed
                        note_distance_from_top = note_timestamp * self.note_speed
                        y_offset = self.track_bar_height - note_distance_from_top
                        render.place(note_drawable, x=note_xoffset, y=y_offset)

            
            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            pass

        def visit(self):
            return self.drawables

        def get_active_notes_per_track(self, current_time):
            active_notes = {
                track_idx: [] for track_idx in range(self.num_track_bars)
            }

            for onset, track_idx in zip(self.onset_times, self.random_track_indices):
                #determine if this note should appear on the track
                time_before_appearance = onset - current_time
                if time_before_appearance < 0: #already below the bottom of the screen
                    continue
                #should be on screen
                #recall that self.note_offset is 3 seconds, the notes' lifespan
                elif time_before_appearance <= self.note_offset:
                    active_notes[track_idx].append((onset, time_before_appearance))
                #there is still time before the next note should show
                #break out of the loop so we don't process subsequent notes that are even further up
                elif time_before_appearance > self.note_offset:
                    break

            return active_notes
