# Legend
* FIX: A bug fix.  Relevant to users and developers.
* NEW: A new feature. Relevant to users and developers.
* SYS: A system-level change.  Usually only relevant to developers.

# v2.24
* FIX: GROUP MODIFIERS > Random and jitter transforms were generating repeating sequences (especially for certain values of the operand).

# v2.23
* NEW: CONFIG.INI > hold-cv-(a,b)-on-zero-gate > Use this setting to have a (normally non-hold) step hold the output CV when its gate is zero.  The default is to only hold the step when the gate becomes zero due to the action of a group modifier.

# v2.22
* FIX: Sometimes the display does not leave the INSERT screen after releasing the INSERT button.
* FIX: Make LAST message appear shorter when trying to scroll past the last step or pattern or part.
* FIX: Parts > Parts would activate immediately when using transition type ‘first’ and at least one track was empty. Now empty tracks are ignored when waiting for the first track to end.
* FIX: Group Modifier > Steps that should have a zero duration as the result of a group modifier would still play for 1 clock pulse.
* FIX: Real-time recording > Only the last pattern recorded was being assigned to the target part.
* NEW: Real-time recording > Newly recorded part is now activated upon punching out. This behavior can be disabled in CONFIG.INI (activate-part).
* NEW: Real-time recording > The next part will be focused upon punching out. This behavior can be disabled in CONFIG.INI (focus-next).
* NEW: CONFIG.INI > user-transition > Added new values for this setting that allow specifying the exact track to use for triggering part transitions.
* NEW: CONFIG.INI > cv-(X,Y,Z)-gated > Gating of the mod CV channels can now be configured separately for each mod channel.
* NEW: CONFIG.INI > cv-(X,Y,Z)-slope-mod > Setting mod CV effect to pre- or post-lookup can now be configured separately for each mod channel and each track.
* NEW: CONFIG.INI > cv-(X,Y,Z)-hold > Setting mod CV hold behavior can now be configured separately for each mod channel and each track.
* NEW: CONFIG.INI > Created configuration groups for each track (1-4) and moved all track-specific settings to these new configuration groups.
* NEW: Held Steps > Steps can be individually set to hold their track’s previously output CV-A or CV-B value. Simply, set the CV-A or CV-B parameter to Hold(Hd) by decrementing further past zero.

# v2.21
* FIX: Some edit operations were mistakenly disabled in HOLD mode since v2.20.

# v2.20
* FIX: Step recording mode > D-2 (delete) is not doing anything.
* FIX: INSERT & DELETE on steps/patterns/tracks should not be allowed in FOLLOW mode (i.e. it should TILT).
* FIX: Browsing through snapshots or voltage tables (things that cause SD card access), intermittently freezes output rendering.

# v2.19
* FIX: Browsing through reference tables or snapshots rapidly would sometimes cause a clock pulse to be missed and hence lose sync.
* FIX: While in HOLD mode, pressing COMMIT when the COPY LED is flashing would cause corruption of the sequence and eventually a crash.
* FIX: CONFIG.INI:Groups:hold-mod-cv was letting mod CV through when the track gate was low rather than holding it.

# v2.18
* FIX: Inconsistent rendering of triggers (especially when duration < 0.2ms) since v2.14.

# v2.17
* NEW: Scala files are now supported. Follow the same naming convention as the binary voltage files (i.e. names are 4 characters long) and use the .SCL extension. For example, dropping a file called TEST.SCL in ER-102/TABLES would be interpreted as a Scala file and show up as tESt in the VOLTAGE display.
* NEW: The root (or key) of the note display is now configurable in the track configuration screen. In the track configuration screen, turn the RIGHT knob to set the root note when you have CV-A or CV-B focused.

# v2.16
* FIX: Copying sequence of steps (as opposed to patterns) should not include pattern boundaries.
* NEW: Added step record config screen containing: CV-A and CV-B voltage zeroing. DURATION and GATE quantization.
* NEW: CONFIG.INI > (Groups:hold-mod-cv) Sample-and-hold any effects from mod CV when a track's gate is high.

# v2.15
* FIX: Dropped gate when clock precedes the reset signal.

# v2.14
* FIX: Incorrect timing info sent from ER-102-to-ER-101 when GATE=DURATION (portato).
* NEW: CONFIG.INI > (Parts:user-transition) New user transition type called 'clock' which causes the next part to play on the next clock pulse.

# v2.13
* FIX: occasionally lost sync (by one clock pulse) when reset.

# v2.12
* NEW: CONFIG.INI > gate-mod-cv can be used to enable(default)/disable the gating of the mod CV effect with its corresponding mod GATE input.

# v2.11
* FIX: Crash (introduced in v2.10) when loading snapshot under the following conditions: unpaused, EDIT/FOLLOW mode, clock is present.  

# v2.10
* FIX: Optimized SD card reading so that loading a snapshot doesn't interfere with the sequencer's ability to stay in sync with external clock and reset signals.

# v2.09
* NEW: CONFIG.INI > load-snapshot-on-boot can be used to fine-tune what snapshot your ER-102 loads on boot up.  The default is for the ER-102 to load the last saved or loaded (i.e. accessed) snapshot. If you want your snapshot load times to be as fast as possible then be sure to use the 'disabled' or 'last-saved' setting.
* NEW: CONFIG.INI > card-read-mode and card-write-mode can be used to tweak how the ER-102 reads or writes to the SD card.  The recommended setting is 'robust'

# v2.08
* NEW: CONFIG.INI > cv-slope-modifier can be used to change the slope modifier to be applied before the voltage lookup instead of after.

# v2.07
* FIX: Hi/Lo transforms on GATE and DURATION were accidentally disabled in v2.06 of the firmware.  Reenabled now.

# v2.06
* NEW: Show number of pulses (nP) when focus pressing the PATTERN or TRACK.
* FIX: CV outputs overflow when clock divider > 1 and SMOOTH is enabled.
* FIX: While editing a MATH transform, the focus LED (orange) gets turned off when you push the RESET button or receive a gate on the RESET input.
* FIX: Cannot browse the indices of an empty track's voltage table.

# v2.05
* NEW: The HIGH/LOW transform screens now use the same UI logic as the other MATH transform screens.
* FIX: Math transform gets mistakenly applied when pinning the math screen.
* FIX: While editing the HIGH/LOW transforms, the GROUP display does not update when turning the LEFT knob.
* FIX: While editing math transform, left focus LED turns off when LOAD button pressed.
* FIX: CONFIG.INI parser made more robust against unusual formatting caused by copy-and-paste from PDF files.

# v2.03
* FIX: Powering up in EJECT mode left some parts of internal data uninitialized.

# v2.02
* FIX: Copying across snapshots in HOLD MODE has bugs.
* FIX: In realtime record config screen, decrementing gate quantization updates duration display.
* FIX: Bug fixes and improvements in the MIDI importer, particularly MIDI files created in Logic.
* FIX: Handle Out-of-memory scenarios more gracefully (particularly MIDI import).
* FIX: Ignore hidden files (resource forks) created by MACOSX.
* NEW: CONFIG.INI > Add 'cents' note display mode.

# v2.01
* FIX: problem with writing data to some uSD cards.

# v2.00
* NEW: Use Euclidean patterns as selection masks when assigning steps to groups.
* NEW: Improved real-time recording experience by recording pass-thru (kind of like auto monitoring). ER-101 is unpaused and a track is armed for recording, however we are punched out.  In this case, the ER-101 will play the existing material on the track but as soon as you play a note (i.e. any event from the record section that would create a note), then the ER-101 switches over to passing through your live playing.  The ER-101/102 remains in this pass-through mode until you pause or unarm or reset.  Of course, at any time you can punch in to begin recording and then punch out again to return to the beginning of this paragraph.
* NEW: A sequencer RESET also punches out.
* NEW: Added all improvements from ER-101 firmware v2.04.
* NEW: MIDI import algorithm is greatly improved: better algorithm for automatically determining MIDI clock divider, and, time quantization setting is now provided.
* NEW: Now able to load up to 4 MIDI files into one snapshot with arbitrary channel to track mapping.
* NEW: CONFIG.INI > no-origin-set = reset-to-step-one | reset-to-loop-start.
* FIX: If the G(mult) parameter of a transform is zero, then the A(dd) parameter changes to the S(et) parameter to emphasize that it will effectively set step parameters rather than add to them.
* FIX: Do the sensible thing when snapshot directory contains only LATEST.BIN (supposedly because the user has manually deleted all of the revision files).
* FIX: Previously, if no LOOP START then use ORIGIN, but it should use the first step instead.
* FIX: If a CONFIG.INI was not on your SD card, then a default one was created but then not loaded until the next time you power up or come out of eject mode.
* FIX: Rotating a group, rotated all groups instead of just the focused group.
* FIX: Some SD cards needed additional coaxing to end a multi-block write command.

# v1.06
* FIX: GATE (slightly) and DURATION (completely) modulation were broken by the v1.04 update.

# v1.05
* FIX: Increased robustness and redundancy in the ER-101 to ER-102 communication system.
* FIX: GATE grid display bug in the real-time configuration screen.

# v1.04
(Warning:  This firmware upgrade will try to convert your v1.02 snapshots to v1.04 snapshots.  However, there is an issue with the conversion process which will corrupt your snapshots.  Please backup your snapshots to your computer and delete the SNAPSHOT directory on your SD card before using the v1.04 firmware.)
* NEW: Improved Snapshots
  * "Focus press" the SNAPSHOT button to get the snapshot description screen where you can use all of the ER-101/102 displays to write your own description/mnemonic for the snapshot.
  * Revision numbers (see the VOLTAGE display when in snapshot description screen).  Snapshots are no longer overwritten when saving.  Instead a new revision is always created and the revision number is incremented.  Recall an earlier version of any snapshot by focusing the revision number, changing it with the RIGHT knob and pressing the LOAD button.
  * A small dot in the SNAPSHOT display indicates whether the slot has a snapshot or not.
  * When updating your firmware, snapshots on your SD card from the previous firmware are automatically converted to the new version.
* NEW: User Voltage tables are now Files 
  * User Voltage tables now live on the SD card.
  * Add as many as you want, just drop a voltage table file into the the ER-102/TABLES directory on  your SD card.
  * Voltage table filenames should be 4 characters long.  These names are shown in the VOLTAGE display when browsing.
  * File format is a simple binary of 100 16-bit (unsigned) integers. Easily creatable from many different scripting languages.
* NEW: Real-time Recording Options
  * Record Focus: In the real-time recording configuration screen, you can set recording to insert after the current step, current pattern, to the end of the track.
  * Assign-to-Part: enable this config file option to have newly recorded material assigned automatically to a part.
  * Wait-for-first-Note:  enable this config file option to have the ER-102 wait for the first note before inserting a step.
* NEW: CONFIG.INI the Configuration File
  * A file called CONFIG.INI will be created in the ER-102 directory of your SD card on first time loading the new firmware.
  * Contains lots of options for customizing the ER-102 to your taste.
  * More options can be easily added according to user's requests without affecting other user's experience.
* NEW: Simultaneous Clock Divide and Multiply
  * Now you can divide the clock as well as multiply the clock.
  * Generate clocks that just multiply or just divide cannot achieve, such as 2/3 or 5/7 of the original clock.
  * "Focus press" the TRACK button to get to the track configuration screen and adjust the divider and multiplier amounts.
* NEW: Rotate/Invert Tracks, Patterns, and Parts 
  * Now only the focused parameter is rotated or inverted over the pattern.
  * This means that you can rotate note values but keep the base rhythm (DURATION and GATE) unchanged and vice versa.
* NEW: Invert MATH transforms
  * Hold down the INVERT button while applying a MATH transform to apply its inverse.
  * Press and release the INVERT button while in the MATH edit screen to invert the operations of the current transform.
  * Only inverts the Add and Multiply operations while ignoring the Random and Jitter operators since they have no inverse. 
* NEW: Separate external clocks for each track
  * Typically, all tracks receive their clock signal from the CLOCK input on the ER-101 (aka global).  However, you can also have any track receive its clock from one of the GATE mod inputs (X, Y, and Z).
  * See the config file for instructions on how to setup the clock routing and enable this behavior.
* NEW: Load MIDI files
  * Type 0 and 1 files are supported.
  * MIDI channels 1-4 are mapped to tracks 1-4, other channels are ignored.
  * Configuration options for transpose and MIDI clock divide are available in the config.ini.
* NEW: ADMIN mode
  * Activated when the STORAGE switch is in ADMIN mode. 
  * Press the RESET button on the ER-101 to soft reset the ER-102.
  * Otherwise not really useful for users (yet) but I wanted to tell you about it so that you are not confused by it.
* NEW: Allow edits in FOLLOW mode if paused or active part is the STOP part, or there is no clock.
* NEW:  JITTER and RANDOM operators for GROUP non-destructive transforms!
* NEW:  MATH edit screen behavior changes slightly: After PINning the edit screen you can apply the transform by pressing the MATH button (used to exit the edit screen). To exit: press the VOLTAGE button (DONE is flashing in the VOLTAGE display).
* FIX: SMOOTH bug when using GROUP modulation
* FIX: TRANSITION bug when in HOLD mode
* FIX: freeze when pasting empty track
* FIX: Non-destructive group transforms now applied to duration/gate only once when a step starts
* NEW: COMMIT while focusing group or group mod, quantizes to pattern
* NEW: COMMIT while focusing part, quantizes to track
* FIX: Quantized RESET, quantized COMMIT, focus-type USER TRANSITION all now save the track that was focused when the quantize was activated.  So even if you navigate to a different track while the RESET/COMMIT/TRANSITION is pending, the original track will still be used to quantize.
* FIX: problem with trigger outputs and ratcheting
