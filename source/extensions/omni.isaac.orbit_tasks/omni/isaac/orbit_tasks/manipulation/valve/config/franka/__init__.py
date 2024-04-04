# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

#from . import agents, env_cfg, mdp, reach_valve_env_cfg
from omni.isaac.orbit_tasks.manipulation.valve import agents, env_cfg, reach_valve_env_cfg
##
# Register Gym environments.
##
#omni.isaac.orbit_tasks.manipulation.valve.reach_valve_env_cfg import ReachValveEnvCfg

gym.register(
        id = "Isaac-Reach-Valve-Franka-v0", 
        #entry_point = "omni.isaac.orbit_tasks.manipulation.valve.reach_valve_env_cfg:ReachValveEnvCfg", # Cfg를 붙임.
        entry_point="omni.isaac.orbit.envs:RLTaskEnv",
        disable_env_checker=True,
        kwargs={
        "env_cfg_entry_point": env_cfg.FrankaReachValveEnvCfg, # env_cfg의 경로를 안 써주어도 되려나...
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:FrankaReachValvePPORunnerCfg",
    },
)
# gym.register(
#     id="Isaac-Reach-Valve-Franka-v0",
#     entry_point="omni.isaac.orbit.envs:RLTaskEnv",
#     disable_env_checker=True,
#     kwargs={
#         "env_cfg_entry_point": env_cfg.FrankaReachValveEnvCfg,
#         "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
#         "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:FrankaReachValvePPORunnerCfg",
#     },
# )

gym.register(
    id="Isaac-Reach-Valve-Franka-Play-v0",
    #entry_point="omni.isaac.orbit_tasks.manipulation.valve.reach_valve_env_cfg:ReachValveEnv", # Cfg를 붙임.
    entry_point="omni.isaac.orbit.envs:RLTaskEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": env_cfg.FrankaReachValveEnvCfg_PLAY,
        "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:FrankaReachValvePPORunnerCfg",
    },
)

# gym.register(
#     id="Isaac-Reach-Valve-Franka-Play-v0",
#     entry_point="omni.isaac.orbit.envs:RLTaskEnv",
#     disable_env_checker=True,
#     kwargs={
#         "env_cfg_entry_point": env_cfg.FrankaReachValveEnvCfg_PLAY,
#         "rl_games_cfg_entry_point": f"{agents.__name__}:rl_games_ppo_cfg.yaml",
#         "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_cfg:FrankaReachValvePPORunnerCfg",
#     },
# )