# Choregraphe simplified export in Python.
def pickup():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0, 2.64])
    keys.append([0, 0])

    names.append("HeadYaw")
    times.append([0, 2.64])
    keys.append([0, 0])

    names.append("LAnklePitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.0670847, -0.00349066, -0.0733038, -0.218166, -0.380482, -0.445059, -0.539307, -0.640536, -0.748746, -0.853466, -0.935496, -1.05767, -1.09781, -1.12752, -1.16413, -1.17286, -1.14494, -1.12225, -1.08909, -1.04894, -1.00007, -0.940732, -0.865683, -0.7662, -0.633555, -0.44855, -0.18326, 0.0828152])

    names.append("LAnkleRoll")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.120026, -0.10821, -0.0959931, -0.0750492, -0.0506146, -0.0401426, -0.0261799, -0.00872665, 0.0174533, 0.0401426, 0.0453786, 0.0541052, 0.0558505, 0.0646891, 0.0698132, 0.0715585, 0.0680678, 0.0680678, 0.0628318, 0.0575959, 0.0471239, 0.0383972, 0.0314159, 0.0174533, -0.00174533, -0.0279253, -0.0645772, -0.100925])

    names.append("LElbowRoll")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([-0.538656, -0.546288, -0.581195, -0.588176, -0.588176, -0.603884, -0.588176, -0.570723, -0.551524, -0.528835, -0.493928, -0.485202, -0.476475, -0.457276, -0.450295, -0.450295, -0.450295, -0.467748, -0.467748, -0.467748, -0.464258, -0.462512, -0.460767, -0.459022, -0.45204, -0.450295])

    names.append("LElbowYaw")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([-1.21233, -1.213, -1.21475, -1.24093, -1.25838, -1.24093, -1.22522, -1.27933, -1.37357, -1.46433, -1.6057, -1.66853, -1.7174, -1.7558, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802, -1.76802])

    names.append("LHand")
    times.append([0, 0.12, 0.4, 0.68, 0.8, 0.92, 1.04, 1.28, 1.4, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.265814, 0.27, 0.29, 0.32, 0.33, 0.33, 0.29, 0.17, 0.1, 0.05, 0.01, 0, 0.01, 0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0, 0, 0])

    names.append("LHipPitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.177174, 0.0802851, -0.0174533, -0.216421, -0.441568, -0.53058, -0.656244, -0.801106, -0.951204, -1.09607, -1.20777, -1.37706, -1.44339, -1.47338, -1.52367, -1.53589, -1.50273, -1.47131, -1.42593, -1.37183, -1.30551, -1.22522, -1.12225, -0.989602, -0.809833, -0.558505, -0.198968, 0.159291])

    names.append("LHipRoll")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.123016, 0.129154, 0.0994838, 0.0767945, 0.0506146, 0.0401426, 0.0244346, 0.00872665, -0.00698132, -0.0244346, -0.0453786, -0.0575959, -0.0610865, -0.0692383, -0.0750492, -0.0767945, -0.0733038, -0.0733038, -0.0680678, -0.0680678, -0.0610865, -0.0523599, -0.0418879, -0.0279253, -0.00872665, 0.0174533, 0.0558505, 0.0953323])

    names.append("LHipYawPitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.156247, -0.16057, -0.165806, -0.176278, -0.18675, -0.191986, -0.198968, -0.205949, -0.214676, -0.221657, -0.226893, -0.235619, -0.233874, -0.240911, -0.244346, -0.244346, -0.242601, -0.233874, -0.232129, -0.230383, -0.246091, -0.260054, -0.253073, -0.247837, -0.235619, -0.218166, -0.193732, -0.169793])

    names.append("LKneePitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.0879548, 0.0418879, 0.171042, 0.431096, 0.712094, 0.82205, 0.98262, 1.1589, 1.33692, 1.53414, 1.67726, 1.89368, 1.97746, 2.01645, 2.08043, 2.09614, 2.05251, 1.98444, 1.92684, 1.85703, 1.77325, 1.67028, 1.53938, 1.37008, 1.12399, 0.809833, 0.413643, -0.0865083])

    names.append("LShoulderPitch")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([1.49561, 1.49575, 1.49575, 1.5132, 1.49575, 1.49575, 1.49575, 1.34739, 1.08909, 0.829031, 0.427606, 0.268781, 0.141372, -0.010472, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239])

    names.append("LShoulderRoll")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.194845, 0.195477, 0.202458, 0.205949, 0.207694, 0.20944, 0.20944, 0.195477, 0.172788, 0.150098, 0.113446, 0.0907571, 0.0907571, 0.0785398, 0.0663225, 0.0610865, 0.0593412, 0.0610865, 0.0575959, 0.0541052, 0.0541052, 0.0471239, 0.0558505, 0.0418879, -0.010472, -0.0296706])

    names.append("LWristYaw")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.107378, 0.106465, 0.0994838, 0.0994838, 0.0994838, 0.0994838, 0.0994838, 0.0942478, 0.0890118, 0.101229, 0.116937, 0.101229, 0.120428, 0.125664, 0.125664, 0.125664, 0.125664, 0.125664, 0.125664, 0.125664, 0.143117, 0.141372, 0.139626, 0.125664, 0.125664, 0.125664])

    names.append("RAnklePitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.0775232, -0.00349066, -0.0733038, -0.218166, -0.380482, -0.445059, -0.539307, -0.640536, -0.748746, -0.853466, -0.935496, -1.05767, -1.09781, -1.12752, -1.16413, -1.17286, -1.14494, -1.12225, -1.08909, -1.04894, -1.00007, -0.940732, -0.865683, -0.7662, -0.633555, -0.44855, -0.18326, 0.0815596])

    names.append("RAnkleRoll")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.0670713, 0.10821, 0.0959931, 0.0750492, 0.0506146, 0.0401426, 0.0261799, 0.00872665, -0.0174533, -0.0401426, -0.0453786, -0.0541052, -0.0558505, 0.0646891, -0.0698132, -0.0715585, -0.0680678, -0.0680678, -0.0628318, -0.0575959, -0.0471239, -0.0383972, -0.0314159, -0.0174533, 0.00174533, 0.0279253, 0.0645772, 0.104293])

    names.append("RElbowRoll")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.453023, 0.546288, 0.581195, 0.588176, 0.588176, 0.603884, 0.588176, 0.570723, 0.551524, 0.528835, 0.493928, 0.485202, 0.476475, 0.457276, 0.450295, 0.450295, 0.450295, 0.467748, 0.467748, 0.467748, 0.464258, 0.462512, 0.460767, 0.459022, 0.45204, 0.450295])

    names.append("RElbowYaw")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([1.29306, 1.213, 1.21475, 1.24093, 1.25838, 1.24093, 1.22522, 1.27933, 1.37357, 1.46433, 1.6057, 1.66853, 1.7174, 1.7558, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802, 1.76802])

    names.append("RHand")
    times.append([0, 0.12, 0.4, 0.68, 0.8, 0.92, 1.04, 1.28, 1.4, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.309811, 0.27, 0.29, 0.32, 0.33, 0.33, 0.29, 0.17, 0.1, 0.05, 0.01, 0, 0.01, 0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0, 0, 0])

    names.append("RHipPitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([0.16577, 0.0802851, -0.0174533, -0.216421, -0.441568, -0.53058, -0.656244, -0.801106, -0.951204, -1.09607, -1.20777, -1.37706, -1.44339, -1.47338, -1.52367, -1.53589, -1.50273, -1.47131, -1.42593, -1.37183, -1.30551, -1.22522, -1.12225, -0.989602, -0.809833, -0.558505, -0.198968, 0.144597])

    names.append("RHipRoll")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.0641347, -0.129154, -0.0994838, -0.0767945, -0.0506146, -0.0401426, -0.0244346, -0.00872665, 0.00698132, 0.0244346, 0.0453786, 0.0575959, 0.0610865, -0.0692383, 0.0750492, 0.0767945, 0.0733038, 0.0733038, 0.0680678, 0.0680678, 0.0610865, 0.0523599, 0.0418879, 0.0279253, 0.00872665, -0.0174533, -0.0558505, -0.118403])

    names.append("RHipYawPitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.156247, -0.16057, -0.165806, -0.176278, -0.18675, -0.191986, -0.198968, -0.205949, -0.214676, -0.221657, -0.226893, -0.235619, -0.233874, -0.240911, -0.244346, -0.244346, -0.242601, -0.233874, -0.232129, -0.230383, -0.246091, -0.260054, -0.253073, -0.247837, -0.235619, -0.218166, -0.193732, -0.169793])

    names.append("RKneePitch")
    times.append([0, 0.12, 0.24, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.48, 2.56, 2.64])
    keys.append([-0.0879548, 0.0418879, 0.171042, 0.431096, 0.712094, 0.82205, 0.98262, 1.1589, 1.33692, 1.53414, 1.67726, 1.89368, 1.97746, 2.01645, 2.08043, 2.09614, 2.05251, 1.98444, 1.92684, 1.85703, 1.77325, 1.67028, 1.53938, 1.37008, 1.12399, 0.809833, 0.413643, -0.0865029])

    names.append("RShoulderPitch")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([1.46094, 1.49575, 1.49575, 1.5132, 1.49575, 1.49575, 1.49575, 1.34739, 1.08909, 0.829031, 0.427606, 0.268781, 0.141372, -0.010472, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239, -0.0471239])

    names.append("RShoulderRoll")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([-0.172139, -0.195477, -0.202458, -0.205949, -0.207694, -0.20944, -0.20944, -0.195477, -0.172788, -0.150098, -0.113446, -0.0907571, -0.0907571, -0.0785398, -0.116937, -0.0610865, -0.0593412, -0.0610865, -0.0575959, -0.0541052, -0.0541052, -0.0471239, -0.0558505, -0.0418879, 0.010472, 0.0296706])

    names.append("RWristYaw")
    times.append([0, 0.12, 0.4, 0.56, 0.68, 0.8, 0.92, 1.04, 1.16, 1.28, 1.4, 1.48, 1.56, 1.64, 1.68, 1.76, 1.84, 1.92, 2, 2.08, 2.16, 2.24, 2.32, 2.4, 2.56, 2.64])
    keys.append([0.151017, -0.106465, -0.0994838, -0.0994838, -0.0994838, -0.0994838, -0.0994838, -0.0942478, -0.0890118, -0.101229, -0.116937, -0.101229, -0.120428, -0.125664, -0.125664, -0.125664, -0.125664, -0.125664, -0.125664, -0.125664, -0.143117, -0.141372, -0.139626, -0.125664, -0.125664, -0.125664])

    return names,times,keys