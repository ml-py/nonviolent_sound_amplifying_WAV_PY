import datetime

def TheOnlyHumanReadableDateTimeFormatString( datetime_object ): # : datetime.datetime) -> str:
    nDT  =  nowDayTime_string  =  str( datetime_object )
    dayOfWeekSlownik  =  {   0: "pon",   1: "wto",   2: "śro",   3: "czw",   4: "pią",
                                                                 5: "sob",   6: "nie"    }
    trzyLiterki  =  dayOfWeekSlownik[  datetime_object.weekday()  ]

    datetime_string_TheOnlyFormat =     nDT[ 2: 4]  +  nDT[ 5: 7]  +  nDT[ 8:10]   \
                                     +  str( trzyLiterki )                         \
                                     +  nDT[11:13]  +  nDT[14:16]  +  nDT[17:19]

    return datetime_string_TheOnlyFormat
TheOnlyTime = TheOnlyHumanReadableDateTimeFormatString

# print(   type( TheOnlyHumanReadableDateTimeFormatString( datetime.datetime.now() ) ),   '\n\n\n'   )
# print(         TheOnlyHumanReadableDateTimeFormatString( datetime.datetime.now() )  ,   '\n\n\n'   )
# print(   type( TheOnlyHumanReadableDateTimeFormatString( datetime.datetime.now() ) ),   '\n\n\n'   )