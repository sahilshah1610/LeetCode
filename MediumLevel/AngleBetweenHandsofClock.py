class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # if (hour==12):
        #     hour =0
        # if (minutes==60):
        #     minutes = 0
        # hour_angle = 0.5 * (hour * 60 + minutes)
        # minute_angle = 6 * minutes
        # angle = abs(hour_angle - minute_angle)
        # angle = min(360 - angle, angle)
        # return angle

        # Method 2
        if hour >= 12:
            hour = hour-12
        hourAngle = float(hour*30)
        print(hourAngle)
        for _ in (range(minutes)):
            hourAngle += .5
        print('after', hourAngle)
        minuteAngle = 6 * minutes
        return abs(hourAngle-minuteAngle)




hour = 3
minutes = 30
objsol = Solution()
print(objsol.angleClock(hour, minutes))
