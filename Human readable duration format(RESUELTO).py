#Your task in order to complete this Kata is to write a function which formats a duration, given as a 
# number of seconds, in a human-friendly way.

#The function must accept a non-negative integer. If it is zero, it just returns "now". 
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

#It is much easier to understand with an example:

#* For seconds = 62, your function should return 
#   "1 minute and 2 seconds"
#* For seconds = 3662, your function should return
#    "1 hour, 1 minute and 2 seconds"

def format_duration(seconds):
    words = ["year", "day", "hour", "minute", "second"]

    if not seconds:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]

        duration = []

        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]

format_duration(457987598)
    



     
