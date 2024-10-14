'''
Hi @technology-team

[IMPORTANT]

Trust we are all doing well. Please spend sometime to look through your objectives for Q3. Kindly complete every outstanding item, ask questions where needed and submit/provide proof of the completed tasks. Also, proceed to start drafting your objectives for Q4. Buzz me if you have any questions. Looking forward to Q4.

See below the grading system
For the velocity objectives, you will find "Deliver 100% of Estimated Capacity (Velocity)" on your Objectives board. How do you rate this on a scale of 1-5.
Exceeded by 50% and above your expected capacity = 5
Exceeded by 30% - 49.99% of your expected capacity = 4.5
Exceeded by 10% - 29.99% of your expected capacity = 4
Exceeded by 1% - 9.99% of your expected capacity = 3.5
Delivered exactly the expected outcome = 3
Fell below expectation by 1% - 9.99% of your expected outcome = 2.5
Fell below expectation by 10% - 29.99% of your expected outcome = 2
Fell below expectation by 30% - 49.99% of your expected outcome = 1.5
Fell below expectation by 50% of your expected outcome = 1

Exceeding Formula: i.e. When Actual is greater than Delta
(Actual - Delta / Delta ) * 100

Fall Below Formula: i.e When Actual is less than Delta
(Delta - Actual / Delta ) * 100

For the other SMART Objectives:
Completed Objectives: 5
Completed only 80% - 99% of the Objectives = 4.5
Completed only 70% - 79% of the Objectives = 4
Completed only 60% - 69% of the Objectives = 3.5
Completed only 50% - 59% of the Objectives = 3
Completed only 40% - 49% of the Objectives = 2.5
Completed only 30% - 39% of the Objectives = 2
Completed only 20% - 29% of the Objectives = 1.5
Completed only 10% - 19% of the Objectives = 1
Completed only 1% - 9% of the Objectives = 0.5
Didn't complete the objectives = 0
'''

actual = float(input("enter actual: \n"))
delta = float(input("enter delta: \n"))

def exceed_or_fall_below_formula(actual: float, delta: float) :
    exceed = False

    if actual > delta:
        velocity = (actual - delta) / delta * 100
        exceed = True
        return (velocity, exceed)

    velocity = (delta - actual) / delta * 100
    return (velocity, exceed)
    
def get_velocity_grade():
    exceed_or_fall_below_result = exceed_or_fall_below_formula(actual, delta)

    match exceed_or_fall_below_result:
        case (velocity, True) if velocity >= 50:
            print(f"Grade 5")
        case (velocity, True) if velocity >= 30 and velocity < 50:
            print(f"Grade 4.5")
        case (velocity, True) if velocity >= 10 and velocity < 30:
            print(f"Grade 4")
        case (velocity, True) if velocity >= 1 and velocity < 10:
            print(f"Grade 3.5")
        case (velocity, False) if velocity == 0: # cannot be `True` because actual - delta = 0 (that is, actual > delta is `False`)
            print(f"Grade 3")
        case (velocity, False) if velocity >= 1 and velocity < 10:
            print(f"Grade 2.5")
        case (velocity, False) if velocity >= 10 and velocity < 30:
            print(f"Grade 2")
        case (velocity, False) if velocity >= 30 and velocity < 50:
            print(f"Grade 1.5")
        case (velocity, False) if velocity >= 50:
            print(f"Grade 1")
        case _:
            print(f"No match found for actual: {actual} and delta: {delta}")
            return

def get_other_smart_objectives_grade(): #WIP
    completed_objectives = float(input("enter completed objectives: \n"))
    match completed_objectives:
        case completed_objectives if completed_objectives >= 5:
            print(f"Grade 5")
        case completed_objectives if completed_objectives >= 4 and completed_objectives < 5:
            print(f"Grade 4.5")
        case completed_objectives if completed_objectives >= 3 and completed_objectives < 4:
            print(f"Grade 4")
        case completed_objectives if completed_objectives >= 2 and completed_objectives < 3:
            print(f"Grade 3.5")
        case completed_objectives if completed_objectives >= 1 and completed_objectives < 2:
            print(f"Grade 3")
        case completed_objectives if completed_objectives >= 0.8 and completed_object