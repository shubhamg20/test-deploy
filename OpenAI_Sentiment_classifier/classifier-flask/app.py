from flask import Flask, render_template, request, jsonify
# import textblob  # Sentiment analysis library
from openai import OpenAI
import re
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

# Function to analyze sentiment using TextBlob
def analyze_text(text):
#   blob = TextBlob(text)
    # sentiment = .2
    
    #Zero shot prompt
    # prompt = f"""Identify the list of labels that the sentence seems to express. The labels are \
    # 'Greetings', 'Backstory', 'Justification', 'Rant', 'Gratitude', 'Other', 'ExpressEmotion. \
    # The sentence is delimitted with tripple backticks \
    # sentence: ```{text}```. your output should be the list of labels without any punctuation and other special chracters"""

    #few shot prompt
    prompt = f"""Identify the list of labels that the sentence seems to express. The labels are \
    'Greetings', 'Backstory', 'Justification', 'Rant', 'Gratitude', 'Other', 'ExpressEmotion. \
    The sentence is delimitted with tripple backticks \
    sentence: ```{text}```. your output should be the list of labels without any punctuation and other special chracters.\
    Here are some examples for your reference:-\
    Example1-
    sentence: ```[Hello, ]just wondering which travel insurance you guys use that really work?[ In the fall we had a two week vacation to Europe, involved four United flights. First got canceled, ergo the second one we missed. Took three other ones instead. On the trip back two flights were planned. Both got canceled even though they were confirmed about three times. Had to take another airline back, skipped last flight and took the train back instead. Had paid for the overseas flight extra for economy plus seats and of course didn't get them since the flight got canceled and we flew with another carrier. Paid $700 for travel insurance, didn't see a penny. Thanks, Undine]```\
       [Greetings, Backstory, Rant, Gratitude]

    Example2-
    sentence:  ```I am traveling with mu husband to Paris out of JFK in Sept. I just changed my seats to the upstairs after reading some reviews. I need to know if we are the last ones off the plane as we have a connecting flight to Naples in an hour.[ I don't want to take the chance of missing my connection.]```\
       [Other]
    Example3-
    sentence: ```Has anyone travelled with Oasis Airlines as yet? [They have fantastic deals to Hong Kong it almost seems too good to be true!]```\
       [ExpressEmotion]
    Example4-
    sentence: ```[I wasn't sure what forfum to post this to so i hope I can get an answer here. I believe there is a site, maybe google, where.... Well let me say what i am looking for. I am going to 5 countries in Europe. I was hoping to look up things to do, restaurants, etc and plot them on a map for myself. There are a lot of preset things with peoples suggestions on the net but would be cool if i had just the stuff on there that I wanted so i can plot out my days.] i have no problem researching and getting the address for things i want i just dont know how to load them on a map with pins or whatever... Can anyone help? [Thanks]```\
       [Backstory, Gratitude, Other]
    Example5-
    sentence: ```[Okay, so we've got the least favourite airline and why thread, so I thought I'd start a favourite airline and why one. ]Our favourite is Singapore Airlines - we've flown Heathrow to New Zealand via Singapore several times and in our opinion, their service is exemplary. [Even in economy. On one occasion I was travelling with my wedding dress and I emailed ahead just to ask how they would advise I carry it. They suggested as hand luggage, but they also very kindly arranged to have a cake and cocktails delivered to us on board. That was really lovely of them. ]Next favourite[ for that hop HRW-AKL] would be Air New Zealand via Hong Kong. Brilliant service, really attentive staff.```\
       [Backstory, Justification]
    Example6-
    sentence: ```I'm looking to fly from Cardiff to Boston with Aer Lingus in March/April 2013, via Dublin. [The Dublin-Boston and return Bosston-Dublin segments are both available and bookable right now, as is the Cardiff-Dublin on the 29th March. ]However the Dublin-Cardiff on 3rd April is unavailable right now. [I'm keen to book asap as I want decent seats on the long segment! ]Anyone have any ideas if their short-haul schedule will be out soon? [It's frustrating as the return date is only 3 days after their current timetable cut-off date!]```\
       [Backstory, ExpressEmotion]
    Example7-
    sentence: ```Just wanna know,if this cheap flights agency,revolution in online travel is real? [because i got my ticket from this agency.]```\
       [Justification]
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )
    output = completion.choices[0].message.content
    output = re.sub(r"[^\w\s]", " ", output).split(" ")
    output = [item for item in output if item]
    print(output)
    return output
    


@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")  # Assuming you have an index.html template


@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
  # Get the text from the request
  text = request.json["text"]

  # Perform sentiment analysis
  sentiment = analyze_text(text)

  return jsonify(success=True, sentiment=sentiment)


if __name__ == "__main__":
  app.run()
