import math
import random
import statistics
from dataclasses import dataclass
from typing import Dict, Iterator, List, Literal, Optional, Tuple

import altair
from ps2_census.enums import FireModeType, PlayerState

from ps2_analysis.altair_utils import (
    SIMULATION_POINT_TYPE_COLOR,
    SIMULATION_POINT_TYPE_SELECTION,
    X,
    Y,
)
from ps2_analysis.geometry_utils import determine_planetman_hit_location
from ps2_analysis.utils import damage_to_kill, float_range

from .ammo import Ammo
from .cone_of_fire import ConeOfFire
from .damage_profile import DamageLocation, DamageProfile
from .fire_timing import FireTiming
from .heat import Heat
from .projectile import Projectile
from .recoil import Recoil

srandom = random.SystemRandom()


@dataclass
class FireMode:
    # Basic information
    fire_mode_id: int
    type: FireModeType
    description: str
    is_ads: bool
    detect_range: float

    # Movement modifiers
    move_multiplier: float
    turn_multiplier: float

    # Damage profiles
    direct_damage_profile: Optional[DamageProfile]
    indirect_damage_profile: Optional[DamageProfile]

    # Zoom
    zoom: float

    # Sway
    sway_can_steady: Optional[bool]
    sway_amplitude_x: Optional[float]
    sway_amplitude_y: Optional[float]
    sway_period_x: Optional[float]
    sway_period_y: Optional[float]

    # Ammo
    ammo: Optional[Ammo]

    # Heat
    heat: Optional[Heat]

    # Fire timing
    fire_timing: FireTiming

    # Recoil
    recoil: Recoil

    # Projectile
    projectile: Optional[Projectile]

    # Player state cones of fire
    player_state_cone_of_fire: Dict[PlayerState, ConeOfFire]

    # Player state can ads
    player_state_can_ads: Dict[PlayerState, bool]

    @property
    def max_consecutive_shots(self) -> int:

        max_consecutive_shots: int

        if self.heat:

            max_consecutive_shots = self.heat.shots_before_overheat

        elif self.ammo:

            max_consecutive_shots = self.ammo.shots_per_clip

        else:

            raise ValueError("No Ammo nor Heat available")

        return max_consecutive_shots

    @property
    def reload_time(self) -> int:

        reload_time: int

        if self.heat:

            reload_time = self.heat.recovery_time(
                heat=self.max_consecutive_shots * self.heat.heat_per_shot
            )

        elif self.ammo:

            reload_time = self.ammo.long_reload_time

        else:

            raise ValueError("No Ammo nor Heat available")

        return reload_time

    @property
    def shots_per_minute(self) -> int:

        shots: int
        time: int
        spm: int

        if (
            self.fire_timing.burst_length
            and self.fire_timing.burst_length > 1
            and self.fire_timing.burst_refire_time
        ):

            shots = self.fire_timing.burst_length
            time = (
                shots - 1
            ) * self.fire_timing.burst_refire_time + self.fire_timing.refire_time

        elif self.max_consecutive_shots > 1:

            shots = 1
            time = self.fire_timing.refire_time + (self.fire_timing.chamber_time or 0)

        else:

            shots = 1
            time = (
                self.fire_timing.total_delay
                + self.fire_timing.refire_time
                + (self.fire_timing.chamber_time or 0)
            )

        if time > 0:

            spm = int(math.floor(60_000 * shots / time))

        else:

            spm = 0

        return spm

    def damage_per_pellet(
        self, distance: float, location: DamageLocation = DamageLocation.TORSO
    ) -> int:

        direct_damage: int = 0

        if self.direct_damage_profile:

            direct_damage = self.direct_damage_profile.damage_per_pellet(
                distance=distance, location=location
            )

        indirect_damage: int = 0

        if self.indirect_damage_profile:

            indirect_damage = self.indirect_damage_profile.damage_per_pellet(
                distance=0, location=location
            )

        return direct_damage + indirect_damage

    def damage_per_shot(
        self, distance: float, location: DamageLocation = DamageLocation.TORSO
    ) -> int:

        direct_damage: int = 0

        if self.direct_damage_profile:

            direct_damage = self.direct_damage_profile.damage_per_shot(
                distance=distance, location=location
            )

        indirect_damage: int = 0

        if self.indirect_damage_profile:

            indirect_damage = self.indirect_damage_profile.damage_per_shot(
                distance=0, location=location
            )

        return direct_damage + indirect_damage

    def shots_to_kill(
        self,
        distance: float,
        location: DamageLocation = DamageLocation.TORSO,
        health: int = 500,
        shields: int = 500,
        damage_resistance: float = 0.0,
    ) -> int:

        dps: int = self.damage_per_shot(distance=distance, location=location)

        if dps > 0:

            return int(
                math.ceil(
                    damage_to_kill(
                        health=health,
                        shields=shields,
                        damage_resistance=damage_resistance,
                    )
                    / dps
                )
            )

        else:

            return -1

    def shots_to_kill_ranges(
        self,
        location: DamageLocation = DamageLocation.TORSO,
        health: int = 500,
        shields: int = 500,
        damage_resistance: float = 0.0,
        step: float = 0.1,
        precision_decimals: int = 2,
    ) -> List[Tuple[float, int]]:

        stk_ranges: List[Tuple[float, int]] = []

        if self.direct_damage_profile:
            if self.direct_damage_profile.damage_range_delta > 0:
                previous_stk: Optional[int] = None

                for r in float_range(
                    0,
                    self.direct_damage_profile.min_damage_range + step,
                    step,
                    precision_decimals,
                ):
                    stk: int = self.shots_to_kill(
                        distance=r,
                        location=location,
                        health=health,
                        shields=shields,
                        damage_resistance=damage_resistance,
                    )

                    if previous_stk is None or stk != previous_stk:
                        if r >= step:
                            stk_ranges.append(
                                (round(r - step, precision_decimals), stk)
                            )
                        else:
                            stk_ranges.append((r, stk))

                    previous_stk = stk
            else:

                stk_ranges.append(
                    (
                        0.0,
                        self.shots_to_kill(
                            distance=self.direct_damage_profile.max_damage_range,
                            location=location,
                            health=health,
                            shields=shields,
                            damage_resistance=damage_resistance,
                        ),
                    )
                )

        elif self.indirect_damage_profile:

            stk_ranges.append(
                (
                    0.0,
                    self.shots_to_kill(
                        distance=0,
                        location=location,
                        health=health,
                        shields=shields,
                        damage_resistance=damage_resistance,
                    ),
                )
            )

        return stk_ranges

    def generate_real_shot_timings(
        self,
        shots: int = -1,
        control_time: int = 0,
        auto_burst_length: Optional[int] = None,
    ) -> Iterator[Tuple[int, bool]]:

        if shots == 0:
            raise ValueError("Cannot simulate 0 shots")

        reloads: int = 0
        remaining: int = shots

        last_timing: Tuple[int, bool] = (0, False)

        shot_timings: List[Tuple[int, bool]]

        while shots == -1 or remaining > 0:

            if shots > 0 and remaining < self.max_consecutive_shots:

                shot_timings = [
                    (last_timing[0] + t + (reloads * self.reload_time), b)
                    for t, b in self.fire_timing.generate_shot_timings(
                        shots=remaining,
                        control_time=control_time,
                        auto_burst_length=auto_burst_length,
                    )
                ]

                remaining = 0

            else:

                shot_timings = [
                    (last_timing[0] + t + (reloads * self.reload_time), b)
                    for t, b in self.fire_timing.generate_shot_timings(
                        shots=self.max_consecutive_shots,
                        control_time=control_time,
                        auto_burst_length=auto_burst_length,
                    )
                ]

                reloads += 1

                remaining -= self.max_consecutive_shots

            yield from shot_timings

            last_timing = shot_timings[-1]

    def simulate_shots(
        self,
        shots: int = -1,
        control_time: int = 0,
        auto_burst_length: Optional[int] = None,
        player_state: PlayerState = PlayerState.STANDING,
        recentering: bool = False,
        recentering_response_time: int = 1_000,
        recentering_inertia_factor: float = 0.7,
    ) -> Iterator[Tuple[int, Tuple[float, float], List[Tuple[float, float]]]]:

        if shots == 0:
            raise ValueError("Cannot simulate 0 shots")

        # Cone of fire at player state
        cof: ConeOfFire = self.player_state_cone_of_fire[player_state]

        # Current state
        # Position; start at origin
        curr_x = 0.0
        curr_y = 0.0

        # Recoil parameters
        curr_max_vertical_recoil: float = self.recoil.max_vertical or 0.0
        curr_min_vertical_recoil: float = self.recoil.min_vertical or 0.0
        curr_max_horizontal_recoil: float = self.recoil.max_horizontal or 0.0
        curr_min_horizontal_recoil: float = self.recoil.min_horizontal or 0.0

        # CoF parameters
        curr_cof_angle: float = cof.min_angle * cof.multiplier

        # Loop
        previous_t: int = 0

        # Recentering
        recentering_vectors: List[Tuple[int, Tuple[float, float]]] = []

        t: int
        b: bool
        for t, b in self.generate_real_shot_timings(
            shots=shots, control_time=control_time, auto_burst_length=auto_burst_length
        ):

            delta = t - previous_t

            # Scaling and recoveries
            ############################################################################

            # After first shot, apply scaling and recoveries
            if t > 0:

                # CoF
                ########################################################################

                cof_recovery_delay: int = self.fire_timing.refire_time + (
                    cof.recovery_delay or 0
                )
                min_cof_angle: float = cof.min_angle * cof.multiplier
                max_cof_angle: float = cof.max_angle * cof.multiplier

                # Under recovery delay -- bloom CoF
                if delta <= cof_recovery_delay:

                    # Bloom if didn't reach max value
                    if curr_cof_angle < max_cof_angle:

                        curr_cof_angle += cof.bloom
                        curr_cof_angle = min(curr_cof_angle, max_cof_angle)

                # Above recovery delay -- recover CoF
                elif cof.recovery_rate:

                    curr_cof_angle -= (cof.recovery_rate / 1_000) * (
                        delta - cof_recovery_delay
                    )
                    curr_cof_angle = max(curr_cof_angle, min_cof_angle)

                # Recoil
                ########################################################################

                recoil_recovery_delay: int = self.fire_timing.refire_time + self.recoil.recovery_delay

                # Under recovery delay -- scale recoil
                if delta <= recoil_recovery_delay:

                    # Vertical
                    if self.recoil.vertical_increase > 0:
                        if curr_min_vertical_recoil < curr_max_vertical_recoil:

                            curr_min_vertical_recoil += self.recoil.vertical_increase
                            curr_min_vertical_recoil = min(
                                curr_min_vertical_recoil, curr_max_vertical_recoil
                            )

                    elif self.recoil.vertical_increase < 0:
                        if curr_max_vertical_recoil > curr_min_vertical_recoil:

                            curr_max_vertical_recoil += self.recoil.vertical_increase
                            curr_max_vertical_recoil = max(
                                curr_min_vertical_recoil, curr_max_vertical_recoil
                            )

                    # Min horizontal
                    if self.recoil.min_horizontal_increase < 0:
                        if curr_min_horizontal_recoil > 0:

                            curr_min_horizontal_recoil += (
                                self.recoil.min_horizontal_increase
                            )
                            curr_min_horizontal_recoil = max(
                                0, curr_min_horizontal_recoil
                            )

                    elif self.recoil.min_horizontal_increase > 0:
                        if curr_min_horizontal_recoil < curr_max_horizontal_recoil:

                            curr_min_horizontal_recoil += (
                                self.recoil.min_horizontal_increase
                            )
                            curr_min_horizontal_recoil = min(
                                curr_min_horizontal_recoil, curr_max_horizontal_recoil,
                            )

                    # Max horizontal
                    if self.recoil.max_horizontal_increase > 0:

                        curr_max_horizontal_recoil += (
                            self.recoil.max_horizontal_increase
                        )

                    elif self.recoil.max_horizontal_increase < 0:
                        if curr_max_horizontal_recoil > curr_min_horizontal_recoil:

                            curr_max_horizontal_recoil += (
                                self.recoil.max_horizontal_increase
                            )
                            curr_max_horizontal_recoil = max(
                                curr_min_horizontal_recoil, curr_max_horizontal_recoil,
                            )

                # Above recovery delay and have a recovery rate -- recover recoil
                elif self.recoil.recovery_rate:

                    full_recoil_recovery_delay: int = recoil_recovery_delay + int(
                        math.ceil(
                            math.sqrt(curr_x ** 2 + curr_y ** 2)
                            / (self.recoil.recovery_rate / 1_000)
                        )
                    )

                    # Below full recovery -- partially recover recoil
                    if delta <= full_recoil_recovery_delay:

                        curr_x -= (
                            (delta - recoil_recovery_delay)
                            * (self.recoil.recovery_rate / 1_000)
                            * math.sin(math.atan(curr_x / curr_y))
                        )
                        curr_y -= (
                            (delta - recoil_recovery_delay)
                            * (self.recoil.recovery_rate / 1_000)
                            * math.cos(math.atan(curr_x / curr_y))
                        )

                    # Above full recovery -- recenter to initial position
                    else:

                        curr_x = 0.0
                        curr_y = 0.0

            # Recentering
            ############################################################################
            if recentering is True:

                # Cursor not centered; applying recentering
                if (curr_x, curr_y) != (0.0, 0.0):

                    # Compute average recentering inertia vector
                    recentering_inertia_vectors: List[Tuple[float, float]] = [
                        k[1]
                        for k in filter(
                            lambda v: v[0] >= t - recentering_response_time,
                            recentering_vectors,
                        )
                    ]

                    recentering_average_inertia_x, recentering_average_inertia_y = [
                        sum(z) / len(z) for z in zip(*recentering_inertia_vectors)
                    ] or [0.0, 0.0]

                    # Compute recentering vector as half sum of current cursor position
                    # and average recentering inertia vector
                    recentering_x: float = (
                        (recentering_inertia_factor * recentering_average_inertia_x)
                        - ((1 - recentering_inertia_factor) * curr_x)
                    )
                    recentering_y: float = (
                        (recentering_inertia_factor * recentering_average_inertia_y)
                        - ((1 - recentering_inertia_factor) * curr_y)
                    )

                    recentering_vectors.append((t, (recentering_x, recentering_y)))

                    curr_x += recentering_x
                    curr_y += recentering_y

            # Current result
            ############################################################################

            # Result as a tuple of time, cursor position tuple and pellets positions tuples
            curr_result: Tuple[int, Tuple[float, float], List[Tuple[float, float]]] = (
                t,  # time
                (curr_x, curr_y),  # cursor
                [],  # pellets
            )

            # CoF simulation
            ############################################################################

            cof_h: float
            cof_v: float
            cof_angle: float
            cof_orientation: float

            if curr_cof_angle == 0.0:

                cof_h = 0.0
                cof_v = 0.0

            else:

                cof_angle = srandom.uniform(0, curr_cof_angle)
                cof_orientation = srandom.uniform(0, 360)

                cof_h = cof_angle * math.cos(math.radians(cof_orientation))
                cof_v = cof_angle * math.sin(math.radians(cof_orientation))

            # Individual pellets position
            for _ in range(
                self.direct_damage_profile.pellets_count
                if self.direct_damage_profile is not None
                else 1
            ):

                pellet_h: float
                pellet_v: float
                pellet_angle: float
                pellet_orientation: float

                if cof.pellet_spread:

                    pellet_angle = srandom.uniform(0, cof.pellet_spread)
                    pellet_orientation = srandom.uniform(0, 360)

                    pellet_h = pellet_angle * math.cos(math.radians(pellet_orientation))
                    pellet_v = pellet_angle * math.sin(math.radians(pellet_orientation))

                    curr_result[2].append(
                        (curr_x + cof_h + pellet_h, curr_y + cof_v + pellet_v)
                    )

                else:

                    curr_result[2].append((curr_x + cof_h, curr_y + cof_v))

            # Recoil simulation
            ############################################################################

            # Un-angled vertical recoil amplitude
            recoil_v: float

            if curr_max_vertical_recoil == curr_min_vertical_recoil:

                recoil_v = curr_max_vertical_recoil

            else:

                recoil_v = srandom.uniform(
                    curr_min_vertical_recoil, curr_max_vertical_recoil
                )

            # FSM scaling of un-angled vertical recoil
            if b is True:

                recoil_v *= self.recoil.first_shot_multiplier

            # Un-angled horizontal recoil amplitude
            recoil_h: float

            if curr_max_horizontal_recoil == curr_min_horizontal_recoil:

                recoil_h = curr_max_horizontal_recoil

            else:

                recoil_h = srandom.uniform(
                    curr_min_horizontal_recoil, curr_max_horizontal_recoil
                )

            # Recoil angle
            recoil_a: float

            if (
                (self.recoil.max_angle, self.recoil.min_angle) == (0.0, 0.0)
                or self.recoil.min_angle is None
                or self.recoil.max_angle is None
            ):

                recoil_a = 0.0

            elif self.recoil.max_angle == self.recoil.min_angle:

                recoil_a = self.recoil.max_angle

            else:

                recoil_a = srandom.uniform(self.recoil.min_angle, self.recoil.max_angle)

            # Horizontal recoil direction
            recoil_h_direction: Literal[-1, 1]
            recoil_h_choices: Tuple[Literal[-1, 1], Literal[-1, 1]] = (-1, 1)

            if self.recoil.half_horizontal_tolerance:

                left_bound: float = (
                    (curr_y - self.recoil.half_horizontal_tolerance)
                    / math.tan(math.radians(90 - recoil_a))
                ) if recoil_a != 0.0 else -self.recoil.half_horizontal_tolerance

                right_bound: float = (
                    (curr_y + self.recoil.half_horizontal_tolerance)
                    / math.tan(math.radians(90 - recoil_a))
                ) if recoil_a != 0.0 else self.recoil.half_horizontal_tolerance

                if left_bound <= curr_x <= right_bound:

                    recoil_h_direction = srandom.choice(recoil_h_choices)

                else:

                    if curr_x > right_bound:

                        recoil_h_direction = -1

                    else:

                        recoil_h_direction = 1

            else:

                recoil_h_direction = srandom.choice(recoil_h_choices)

            recoil_h *= recoil_h_direction

            # Angle horizontal and vertical recoil
            recoil_h_angled: float
            recoil_v_angled: float

            if recoil_a == 0.0:

                recoil_h_angled = recoil_h
                recoil_v_angled = recoil_v

            else:

                recoil_h_angled = recoil_h * math.cos(
                    math.radians(recoil_a)
                ) + recoil_v * math.sin(math.radians(recoil_a))

                recoil_v_angled = -recoil_h * math.sin(
                    math.radians(recoil_a)
                ) + recoil_v * math.cos(math.radians(recoil_a))

            # Yield
            yield curr_result

            # Update current position
            curr_x += recoil_h_angled
            curr_y += recoil_v_angled

            previous_t = t

    def damage_inflicted_by_pellets(
        self,
        distance: float,
        pellets: List[Tuple[float, float]],
        aim_location: DamageLocation = DamageLocation.TORSO,
    ) -> int:

        damage: int = 0

        pellet_h_angle: float
        pellet_v_angle: float
        for pellet_h_angle, pellet_v_angle in pellets:
            pellet_x: float = math.tan(math.radians(pellet_h_angle)) * distance
            pellet_y: float = math.tan(math.radians(pellet_v_angle)) * distance

            hit_location: Optional[DamageLocation] = determine_planetman_hit_location(
                x=pellet_x, y=pellet_y, aim_location=aim_location
            )

            damage += (
                self.damage_per_pellet(distance=distance, location=hit_location)
                if hit_location
                else 0
            )

        return damage

    def real_time_to_kill(
        self,
        distance: float = 1.0,
        runs: int = 1,
        max_time: int = 20_000,
        control_time: int = 0,
        health: int = 500,
        shields: int = 500,
        damage_resistance: float = 0.0,
        auto_burst_length: Optional[int] = None,
        aim_location: DamageLocation = DamageLocation.TORSO,
        player_state: PlayerState = PlayerState.STANDING,
        recentering: bool = False,
        recentering_response_time: int = 1_000,
        recentering_inertia_factor: float = 0.7,
    ) -> int:

        if not self.direct_damage_profile and not self.indirect_damage_profile:
            return -1

        ttks: List[int] = []

        dtk: int = damage_to_kill(
            health=health, shields=shields, damage_resistance=damage_resistance
        )

        simulation: Iterator[Tuple[int, Tuple[float, float], List[Tuple[float, float]]]]
        for simulation in (
            self.simulate_shots(
                shots=-1,
                control_time=control_time,
                auto_burst_length=auto_burst_length,
                recentering=recentering,
                recentering_response_time=recentering_response_time,
                recentering_inertia_factor=recentering_inertia_factor,
                player_state=player_state,
            )
            for _ in range(runs)
        ):

            total_damage: int = 0

            t: int
            pellets_coors: List[Tuple[float, float]]
            for t, _, pellets_coors in simulation:

                if t > max_time:

                    break

                total_damage += self.damage_inflicted_by_pellets(
                    distance=distance, pellets=pellets_coors, aim_location=aim_location
                )

                if total_damage >= dtk:

                    ttks.append(t)

                    break

        return int(math.ceil(statistics.median(ttks))) if ttks else -1

    def generate_altair_simulation(
        self,
        shots: int,
        runs: int = 1,
        control_time: int = 0,
        auto_burst_length: Optional[int] = None,
        recentering: bool = False,
        recentering_response_time: int = 1_000,
        recentering_inertia_factor: float = 0.3,
        player_state: PlayerState = PlayerState.STANDING,
    ) -> altair.HConcatChart:

        datapoints: List[dict] = []

        simulation: Iterator[Tuple[int, Tuple[float, float], List[Tuple[float, float]]]]
        for simulation in (
            self.simulate_shots(
                shots=shots,
                control_time=control_time,
                auto_burst_length=auto_burst_length,
                recentering=recentering,
                recentering_response_time=recentering_response_time,
                recentering_inertia_factor=recentering_inertia_factor,
                player_state=player_state,
            )
            for _ in range(runs)
        ):

            t: int
            cursor_coor: Tuple[float, float]
            pellets_coors: List[Tuple[float, float]]
            for t, cursor_coor, pellets_coors in simulation:

                cursor_x, cursor_y = cursor_coor

                datapoints.append(
                    {"Time": t, X: cursor_x, Y: cursor_y, "Type": "cursor"}
                )

                for pellet_x, pellet_y in pellets_coors:
                    datapoints.append(
                        {"Time": t, X: pellet_x, Y: pellet_y, "Type": "pellet"}
                    )

        dataset: altair.Data = altair.Data(values=datapoints)

        chart: altair.Chart = (
            altair.Chart(dataset)
            .mark_point()
            .encode(
                x=altair.X(
                    f"{X}:Q", axis=altair.Axis(title="horizontal angle (degrees)")
                ),
                y=altair.Y(
                    f"{Y}:Q", axis=altair.Axis(title="vertical angle (degrees)")
                ),
                color=SIMULATION_POINT_TYPE_COLOR,
                tooltip="Time:Q",
            )
            .interactive()
        )

        legend: altair.Chart = (
            altair.Chart(dataset)
            .mark_point()
            .encode(
                y=altair.Y("Type:N", axis=altair.Axis(orient="right")),
                color=SIMULATION_POINT_TYPE_COLOR,
            )
            .add_selection(SIMULATION_POINT_TYPE_SELECTION)
        )

        result: altair.HConcatChart = altair.hconcat(chart, legend)

        return result
