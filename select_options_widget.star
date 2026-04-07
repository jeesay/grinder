loop_
_fieldset.id
_fieldset.label
_fieldset.widget
_fieldset.default  # Default value
_fieldset.arg0     # <select> parent
_fieldset.arg1     # None
_fieldset.arg2     # None
_fieldset.help
gain_rot 'Gain rotation:' select 0 ? ? ? 
;Rotate the gain reference by this number times 90 degrees clockwise in relion_display. This is the same as -RotGain in MotionCor2. Note that MotionCor2 uses a different convention for rotation so it says 'counter-clockwise'. Valid values are 0, 1, 2 and 3.
;
no_rot   'No rotation'   option 0 gain_rot ? ? ?
rot_90   '90° rotation'  option 1 gain_rot ? ? ?
rot_180  '180° rotation' option 2 gain_rot ? ? ?
rot_270  '270° rotation' option 3 gain_rot ? ? ?

