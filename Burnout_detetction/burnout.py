print("===== STUDENT BURNOUT DETECTION SYSTEM =====")

def calculate_burnout(sleep_hours, screen_time, breaks_taken):

    burnout_score = 0

    if sleep_hours < 5:
        burnout_score += 40
    elif sleep_hours < 7:
        burnout_score += 20

    if screen_time > 8:
        burnout_score += 30
    elif screen_time >= 5:
        burnout_score += 15

    if breaks_taken <= 1:
        burnout_score += 20
    elif breaks_taken <= 3:
        burnout_score += 10

    if burnout_score >= 60:
        burnout_risk = "HIGH"
    elif burnout_score >= 30:
        burnout_risk = "MODERATE"
    else:
        burnout_risk = "LOW"

    return burnout_score, burnout_risk

def calculate_productivity(
    study_hours,
    sleep_hours,
    screen_time,
    breaks_taken
):

    score = 0

    score += study_hours * 10
    score += sleep_hours * 5
    score -= screen_time * 3
    score += breaks_taken * 2

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score

def calculate_fake_productivity(
    study_hours,
    planning_hours,
    study_video_hours
):

    if study_hours == 0:
        return "HIGH"

    fake_ratio = (
        planning_hours + study_video_hours
    ) / study_hours

    if fake_ratio >= 1:
        return "HIGH"

    elif fake_ratio >= 0.5:
        return "MODERATE"

    else:
        return "LOW"

# Taking Input
study_hours = int(input("Enter the number of hours you study per day: "))
sleep_hours = int(input("Enter the number of hours you sleep per day: "))
screen_time = int(input("Enter screen time (hours per day): "))
breaks_taken = int(input("Enter the number of breaks you take during study sessions: "))
planning_hours = int(input("Enter hours spent planning/studying schedules: "))
study_video_hours = int(input("Enter hours spent watching study videos: "))

burnout_score, burnout_risk = calculate_burnout(
    sleep_hours,
    screen_time,
    breaks_taken
)

score = calculate_productivity(
    study_hours,
    sleep_hours,
    screen_time,
    breaks_taken
)

fake_productivity = calculate_fake_productivity(
    study_hours,
    planning_hours,
    study_video_hours
)

# Display Student Data
print("\n----- STUDENT DATA -----")
print("Study Hours:", study_hours)
print("Sleep Hours:", sleep_hours)
print("Screen Time:", screen_time)
print("Breaks Taken:", breaks_taken)



# Display Result

print("\n----- RESULTS -----")
print("Burnout Risk Level:", burnout_risk)
print("Productivity Score:", score, "/100")
print("Fake Productivity Risk:", fake_productivity)
print("Burnout Score:", burnout_score, "/100")
print("\n----- SUGGESTIONS -----")

if sleep_hours < 7:
    print("- Try to get at least 7-8 hours of sleep.")

if screen_time > 5:
    print("- Reduce daily screen time.")

if breaks_taken < 2:
    print("- Take more breaks while studying.")

if study_hours < 3:
    print("- Increase focused study time.")

if sleep_hours >= 7 and screen_time <= 5:
    print("- Great job! Keep maintaining healthy habits.")