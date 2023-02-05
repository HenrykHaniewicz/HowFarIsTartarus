# Premise: How far is Tartarus from Earth? In the Greek Myth: The Castration of Uranus, it apparently takes a falling anvil 9 days to reach Tartarus from Earth
# I shall first assume g = 9.81 is constant and for the second model assume a constant density through an Earth-like medium (meaning g drops off linearly starting at 9.81)
# I also assume the anvil is in freefall meaning its mass doesn't matter

import numpy as np

def new_velocity( u, a, t ):
    return (u + (a * t))

# Accepts u in ms-1, t in s, g in ms-2
def displacement_constantg( u, t, g ):
    return ((u * t) + 0.5 * g * (t**2))

def displacement_linearg( u, t, dt = 0.001 ):
    g = 9.81
    d = 0
    vel = u
    num_steps = t/dt
    g_decay_factor = g/num_steps
    for time_step in np.arange(0, t, dt):
        d += displacement_constantg( vel, dt, g )
        vel = new_velocity( vel, g, dt )
        g -= g_decay_factor
    return d

def days_2_seconds(days):
    return (days*24*60*60)

def m_2_ly(meters):
    return meters * 1.0570008340247e-16

def m_2_AU(meters):
    return meters * 6.6845871226706e-12



if __name__ == "__main__":
    NUM_DAYS = 9
    init_velocity = 0
    g = 9.81

    dist = displacement_constantg( init_velocity, days_2_seconds(NUM_DAYS), g )
    dist_au = m_2_AU(dist)
    dist_ly = m_2_ly(dist)

    dist_var = displacement_linearg( init_velocity, days_2_seconds(NUM_DAYS) )
    dist_var_au = m_2_AU(dist_var)
    dist_var_ly = m_2_ly(dist_var)

    print( "Constant g = 9.81" )
    print( f"Distance in m: {dist} m" )
    print( f"Distance in AU: {dist_au} AU" )
    print( f"Distance in ly: {dist_ly} ly" )

    print("")

    print( "Constant g decay" )
    print( f"Distance in m: {dist_var} m" )
    print( f"Distance in AU: {dist_var_au} AU" )
    print( f"Distance in ly: {dist_var_ly} ly" )
