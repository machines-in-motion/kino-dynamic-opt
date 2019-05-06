## # TEMP:

import numpy as np
from matplotlib import pyplot as plt


positions = np.loadtxt('quadruped_positions_eff.dat', dtype=float)
velocities = np.loadtxt('quadruped_velocities_eff.dat', dtype=float)
com = np.loadtxt('quadruped_com.dat', dtype=float)
com_vel = np.loadtxt('quadruped_com_vel.dat', dtype=float)
ang_vel = np.loadtxt('quadruped_base_ang_velocities.dat', dtype=float)
forces = np.loadtxt('quadruped_centroidal_forces.dat', dtype=float)
moments = np.loadtxt('quadruped_centroidal_moments.dat', dtype=float)
abs_vel = np.loadtxt('quadruped_velocities_abs.dat', dtype=float)



print(np.shape(positions))

fig, ax = plt.subplots(9,1)
ax[0].plot(positions[:, 0], label = "end_eff_x_pos")
ax[0].plot(positions[:, 1], label = "end_eff_y_pos")
ax[0].plot(positions[:, 2], label = "end_eff_z_pos")
ax[0].set_xlabel("millisec")
ax[0].set_ylabel("m")
ax[0].legend()
ax[0].grid()

ax[1].plot(positions[:, 6], label = "end_eff_x_pos")
ax[1].plot(positions[:, 7], label = "end_eff_x_pos")
ax[1].plot(positions[:, 8], label = "end_eff_x_pos")
ax[1].set_xlabel("millisec")
ax[1].set_ylabel("m")
ax[1].legend()
ax[1].grid()

ax[2].plot(positions[:, 12], label = "end_eff_x_traj")
ax[2].plot(positions[:, 13], label = "end_eff_y_traj")
ax[2].plot(positions[:, 14], label = "end_eff_z_traj")
ax[2].set_xlabel("millisec")
ax[2].set_ylabel("m")
ax[2].legend()
ax[2].grid()

ax[3].plot(positions[:, 18], label = "end_eff_x_traj")
ax[3].plot(positions[:, 19], label = "end_eff_x_traj")
ax[3].plot(positions[:, 20], label = "end_eff_x_traj")
ax[3].set_xlabel("millisec")
ax[3].set_ylabel("m")
ax[3].legend()
ax[3].grid()

ax[4].plot(com[:, 1], label = "com_vel_x")
ax[4].plot(com[:, 2], label = "com_vel_y")
ax[4].plot(com[:, 3], label = "com_vel_z")
ax[4].set_xlabel("millisec")
ax[4].set_ylabel("m")
ax[4].legend()
ax[4].grid()

#ax[5].plot(forces[:, 1], label = "Fx")
#ax[5].plot(forces[:, 2], label = "Fy")
#ax[5].plot(forces[:, 3], label = "Fz")
ax[5].plot(abs_vel[:, 1], label = "abs_x")
ax[5].plot(abs_vel[:, 2], label = "abs_y")
ax[5].plot(abs_vel[:, 3], label = "abs_z")

ax[5].set_xlabel("millisec")
ax[5].set_ylabel("m")
ax[5].legend()
ax[5].grid()

#ax[6].plot(forces[:, 4], label = "Fx")
#ax[6].plot(forces[:, 5], label = "Fy")
#ax[6].plot(forces[:, 6], label = "Fz")
ax[6].plot(abs_vel[:, 4], label = "abs_x")
ax[6].plot(abs_vel[:, 5], label = "abs_y")
ax[6].plot(abs_vel[:, 6], label = "abs_z")
ax[6].set_xlabel("millisec")
ax[6].set_ylabel("m")
ax[6].legend()
ax[6].grid()

#ax[7].plot(forces[:, 7], label = "Fx")
#ax[7].plot(forces[:, 8], label = "Fy")
#ax[7].plot(forces[:, 9], label = "Fz")
ax[7].plot(abs_vel[:, 7], label = "abs_x")
ax[7].plot(abs_vel[:, 8], label = "abs_y")
ax[7].plot(abs_vel[:, 9], label = "abs_z")
ax[7].set_xlabel("millisec")
ax[7].set_ylabel("m")
ax[7].legend()
ax[7].grid()

#ax[8].plot(forces[:, 10], label = "Fx")
#ax[8].plot(forces[:, 11], label = "Fy")
#ax[8].plot(forces[:, 12], label = "Fz")
ax[8].plot(abs_vel[:, 10], label = "abs_x")
ax[8].plot(abs_vel[:, 11], label = "abs_y")
ax[8].plot(abs_vel[:, 12], label = "abs_z")
ax[8].set_xlabel("millisec")
ax[8].set_ylabel("m")
ax[8].legend()
ax[8].grid()

fig1, ax1 = plt.subplots(2,1)
ax1[0].plot(forces[:, 1], label = "com_force_x")
ax1[0].plot(forces[:, 2], label = "com_force_y")
ax1[0].plot(forces[:, 3], label = "com_force_z")
ax1[0].set_xlabel("millisec")
ax1[0].set_ylabel("m")
ax1[0].legend()
ax1[0].grid()

ax1[1].plot(moments[:, 1], label = "com_moments_x")
ax1[1].plot(moments[:, 2], label = "com_moments_y")
ax1[1].plot(moments[:, 3], label = "com_moments_z")
ax1[1].set_xlabel("millisec")
ax1[1].set_ylabel("m")
ax1[1].legend()
ax1[1].grid()



plt.show()
