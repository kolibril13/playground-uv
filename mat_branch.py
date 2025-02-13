# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib @ git+https://github.com/skkestrel/matplotlib.git@6fa3ddc2fa7cf82e1feb2f7d0d22d79bcbe88449",
# ]
# ///


import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].plot([5, 2, 8], label='long\nlabel')
ax[0].plot([4, 9, 1], label='another\nlong\nlabel')
ax[0].legend(title="align=baseline (default)")

ax[1].plot([5, 2, 8], label='long\nlabel')
ax[1].plot([4, 9, 1], label='another\nlong\nlabel')
ax[1].legend(title="align=top", itemboxalign='top')

plt.show()

