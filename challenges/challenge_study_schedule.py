def study_schedule(persistence_periods, target_time):
    if target_time is None:
        return None

    student_count = 0
    for start_period, end_period in persistence_periods:
        if not isinstance(start_period, int) \
              or not isinstance(end_period, int):
            return None

        if start_period <= target_time <= end_period:
            student_count += 1

    return student_count
