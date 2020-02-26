from gym.envs.registration import registry, register, make, spec

register(
    id='Zork1-v0',
    entry_point='envs.jericho_env:Zork1JerichoEnv',
    max_episode_steps=1000
)

register(
    id='Zork2-v0',
    entry_point='envs.jericho_env:Zork2JerichoEnv',
    max_episode_steps=1000
)

register(
    id='Zork3-v0',
    entry_point='envs.jericho_env:Zork3JerichoEnv',
    max_episode_steps=1000
)

register(
    id='905-v0',
    entry_point='envs.jericho_env:Nine05JerichoEnv',
    max_episode_steps=1000
)

register(
    id='AcornCourt-v0',
    entry_point='envs.jericho_env:AcornCourtJerichoEnv',
    max_episode_steps=1000
)

register(
    id='Advent-v0',
    entry_point='envs.jericho_env:AdventJerichoEnv',
    max_episode_steps=1000
)

register(
    id='AdventureLand-v0',
    entry_point='envs.jericho_env:AdventureLandJerichoEnv',
    max_episode_steps=1000
)

register(
    id='Afflicted-v0',
    entry_point='envs.jericho_env:AfflictedJerichoEnv',
    max_episode_steps=1000
)

register(
    id='Anchor-v0',
    entry_point='envs.jericho_env:AnchorJerichoEnv',
    max_episode_steps=1000
)

register(
    id='Awaken-v0',
    entry_point='envs.jericho_env:AwakenJerichoEnv',
    max_episode_steps=1000
)
