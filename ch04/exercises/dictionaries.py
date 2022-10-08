article = """
The Try Guys are going to try being a trio. The group, which gained popularity at Buzzfeed for their viral videos and eventually departed to begin producing content through their own company, announced on Tuesday that founding member Ned Fulmer “is no longer working with The Try Guys.”
“As a result of a thorough internal review, we do not see a path forward together,” a statement posted to social media said. “We thank you for your support as we navigate this change.” 
The statement did not elaborate on the nature of the review. 
Fulmer, who with Keith Habersberger, Zach Kornfeld, and Eugene Lee Yang was a founding member, had been the subject of speculation-filled chatter on Reddit and other social media platforms prior to his ouster regarding allegations of infidelity. 
In a statement posted to Instagram, Fulmer said he had “a consensual workplace relationship.” “I’m sorry for any pain that my actions may have caused to the guys and the fans but most of all Ariel,” he wrote. “The only thing that matters right now is my marriage and my children, and that’s where I am going to focus my attention.” 
"""


substitutions = {
  "Ned":"Pit of Despair",
  "consensual":"sad",
  "member":"puppy",
  "Try Guys":"Cool People Minus Ned"
}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)