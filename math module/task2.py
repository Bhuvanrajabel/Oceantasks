Students=[
    {"Name":"Rohit","Scores":[95,88,92]},
    {"Name":"Kohli","Scores":[72,65,70]},
    {"Name":"Dhoni","Scores":[60,58,64]}
]
for Data in Students:
    Students_name=Data["Name"]
    Students_Score=Data["Scores"]
    sum=0
    for i in Students_Score:
        sum+=i
    avg=sum/len(Students_Score)
    if avg>=85:
        Score=" Very Good"
    elif avg>=70:
        Score="Good"
    elif avg>=50:
        Score="Average"
    else:
        Score="Poor"
    print(Students_name,int(avg),Score)