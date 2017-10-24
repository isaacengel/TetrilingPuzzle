# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: PERFORMANCE TEST
# Author: Liuqing Chen, Feng Shi, Isaac Engel (13th September 2017)
# Last updated: 13th September 2017
# ####################################################

import matplotlib.pyplot as plt
import solution_v7_screensaver as isaac_solution
import utils_v2 as utils

plt.ion()
fig = plt.figure()

while(True):
    target = utils.generate_target(width=10, height=10, density=0.6)  # NOTE: it's recommended to keep density below 0.8
    solution = isaac_solution.solution(target,fig)
    plt.pause(1)
    fig.clf()
