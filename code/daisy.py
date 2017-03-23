nosc              = 22.0 # 22 radial oscillations for closed Daisy pattern
map_radius        = 2.8  # arc-minutes
radial_osc_period = 25.0 # seconds
n_scans           = 5    # split 22 oscillations over 5 scans
scanDuration      = nosc * radial_osc_period / n_scans
phi2              = 2.0 * nosc / n_scans
phi1              = 3.14159265 * phi2
#NOTE - increment rotation_phase by phi2 each scan
#     - increment radial_phase by phi1 each scan
for i in range(n_scans):
  Daisy('3C123',map_radius,radial_osc_period,i*phi1,i*phi2,scanDuration,
        beamName='1',coordMode='J2000',cos_v=True,calc_dt=0.2)
