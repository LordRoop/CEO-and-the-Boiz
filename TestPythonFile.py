import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

temp = None

def set_temp(inItTemp):
    global temp
    temp = inItTemp

set_temp(1)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temp, # this is the degree of randomness of the model's output
    )
    print("\nTemprature: " + str(temp) + "\n")
    return response.choices[0].message["content"]

# def get_location():

text = f"""
Over the last 20 years, the science of happiness has emerged as widely studied discipline with implications for everyday life. Some people say happiness is a choice, while others believe it's innate. According to social psychologist Sonja Lyubomirsky, a professor at the University of California, Riverside, the truth lies somewhere in the middle, with 50% of happiness being determined by our genes, 10% by our circumstances, and 40% by our actions, attitude, and responses to life's inevitable ups and downs.

Learn About The Science Of Happiness
Connect With An Online Therapist

Happiness Defined

Lyubomirsky, a social psychologist, can define happiness as “joy, contentment, or positive well-being, combined with a sense that one's life is good, meaningful, and worthwhile.”

Many researchers swap the word "happiness" with the term "subjective well-being," inferring that two people experiencing identical circumstances may rate themselves at opposite ends of a happiness rating scale.

In fact, some experts believe that individuals have a happiness set point, which is determined early in life and largely unaffected by life circumstances over the long term. This theory isn't conclusive, and some research suggests we may have more control over our happiness than some set-point theorists give us credit for.

As the "Father of American Psychology," William James once said, "The greatest discovery… is that human beings can alter their lives by altering their attitudes…"
A Recipe For Happiness

So, what is it that makes people truly happy? Research suggests that happy people have several things in common. From prioritizing happiness to practicing mindfulness, gratitude, and compassion, the way we live our daily lives can greatly impact the level of happiness we experience.

The following are nine habits of happy people that may elevate your level of happiness significantly:
1. Practice Gratitude

What is gratitude? "Gratitude" is a feeling associated with appreciation. Research shows that a gratitude practice helps us appreciate the little things in life, shifting our thoughts from what we think is lacking to what's positive and abundant. Keeping a gratitude journal may be an effective way to facilitate that shift. You don't necessarily have to jot down your appreciation on a daily basis. According to Berkeley University's Greater Good Science Center, writing in a gratitude journal just three times a week can be more effective in elevating happiness than jotting down our appreciation daily. For some, the key may be to physically write a gratitude list down, as making a mental note may not have the same positive effects.

The following are several ways to increase the effectiveness of a gratitude practice:

    Being specific when recalling a positive experience, person, or event may help you tap into the depth of your gratitude.

    Being grateful for the people in your life may increase happiness more than recalling places or things.

    Viewing your positive experiences as gifts may help ensure you don’t take them for granted.

    Noting surprises, such as an impromptu visit from a friend or a beautiful rainbow after a storm, may boost your happiness. Unexpected experiences and events can make feelings of gratitude even stronger.

    Trying to avoid repetition may widen your perspective. Changing up your gratitude list may help you feel more grateful. If all of your gratitude lists tend to be similar, try focusing on different aspects of your relationships or experiences.

    Making gratitude a regular practice is key. Whether you jot down what you're thankful for once per week or every other day, it may help to stick to a schedule to reap the most benefits. Some researchers urge people to avoid writing a gratitude list daily, as it may result in numbness to positive experiences and events.

Learn About The Science Of Happiness
Connect With An Online Therapist

2. Pay Attention To The Good, And Don't Dwell On The Bad

Rather than fixating on a negative experience, such as getting an upsetting email or arguing with a friend, you might try zeroing in on the positive aspects of your day. As humans, we're hardwired to focus on bad experiences and completely gloss over good ones. This phenomenon is called negativity bias, and it has the power to diminish our joy and keep our brains on the lookout for distressing news, events, interactions, etc.

Greater awareness may help to combat negativity bias. Making a conscious effort to pay more attention to positive experiences and emotions can be transformative. By consistently practicing the art of focusing on these areas, you may be able to set yourself up for a happier future.
3. Be Mindful

Research has shown that mindfulness can reduce stress and boost overall well-being. Being mindful entails curiosity, non-judgment, and awareness of what's happening in the present moment.

When we're truly present, we aren't focusing on past regrets or what may happen in the future. One strategy for learning to live in the present is by practicing mindfulness meditation, which you can do on your own or with a guided meditation app. 
4. Be More Compassionate

It can be easy to rush through the day trying to complete your to-do list while meeting your basic needs. When you’re constantly on the go, it can be difficult to practice compassion for others and yourself.

Practicing compassion sometimes requires slowing down, which may seem challenging to people with perpetually hectic schedules. However, research shows that slowing down can enables you to get more done while opening up space for contentment and increased compassion.

One way to practice compassion is with guided meditations specifically created for compassion or "lovingkindness." The University of California, Berkeley, offers a free online guided meditation that may be ideal for beginners or anyone looking to increase their level of compassion for themselves and others. The 32-minute session guides participants through a lovingkindness and compassion meditation, first asking them to focus on a loved one, then themselves, followed by a neutral person, an enemy, and finally all living beings. This type of meditation can reduce negativity while elevating kindness, compassion, and well-being.
5. Revel In Your Happiness

A surprising amount of people on their deathbeds wish they had allowed themselves to be happier people throughout their lives. It can be easy to settle into routines without questioning our level of happiness and contentment.

Making an effort to acknowledge our routines and cultivate a more curious mindset may open up a world of new experiences that could lead to newfound happiness.
6. Form And Maintain Relationships

According to an ongoing Harvard study, your social circle could have a significant impact on your happiness level. Positive relationships can lead to better health and increased happiness. These relationships can be with friends, family, or people in your community.

The study has found that loneliness can be toxic, and isolation can lead to poor health, decreased brain functioning, and even earlier death.
7. Learn To Forgive

If you tend to hold grudges, learning to forgive could boost your mood, along with your overall health. Studies show that people who have difficulty forgiving others experience increased negativity, anger, and sadness and feel less in control of their lives. Embracing forgiveness may counteract these negative effects on your mood and overall mental health.

8. Engage In Physical Activity

Physical activity has been linked to an improvement in mood. Even a little bit of exercise can go a long way.

Individuals who engage in physical activity just once or twice a week tend to feel happier than those who are sedentary. Even 10 minutes per session can have a positive impact on mood, and it doesn't seem to matter what type of physical activity people choose. People who engage in 30 minutes or more of physical activity on most days report being 30% happier than people who exercise less.
9. Don't Ignore Your Strengths

As humans, we often hone in on our weaknesses and completely ignore our strengths. Nurturing our strengths, using them, and reflecting on them can boost confidence and self-esteem and lead to increased happiness. Research shows that simply thinking about our strengths has the power to boost happiness and decrease depression.
Embracing All Of Your Emotions

While happiness is a positive, powerful emotion, all people experience a range of emotions. If you implement some of the above strategies, you might also remember to not judge yourself when you experience other emotions. You can work toward happiness while still acknowledging emotions such as joy, contentment, sadness, frustration, anger, and surprise.
Finding Your Happiness

If you're experiencing negative emotions, or if you've tried the tips above and still don't experience happiness, you may benefit from talking to a licensed therapist. If you don’t like the idea of going to a therapy practice, you might try online therapy services, which several studies have shown to be just as effective as in-person therapy. With BetterHelp, you can talk to a therapist from anywhere with an internet connection, and you can change therapists until you find the right fit for you.
Takeaway

If you’re experiencing challenging emotions or if you simply have questions about how to boost happiness, you’re not alone. Thousands of people reach out to a therapist to discuss ways to address these questions. You can be matched with a therapist with experience helping people manage mental health concerns similar to yours, and you can talk to them on a schedule that works for you. Take the first step and reach out to BetterHelp today.
"""

prompt = f"""
Scan the selected text delimited by tripple backticks for main ideas or key points that can be extracted into a brief introductory paragraph and bullet points. 

First, write a brief paragraph containing three main things. One, the tone of the information. Two, what feelings were conveyed in the text.
Three, you must introduce the topic or person being covered. Use only three to five sentances.
This paragraph is only meant for the reader to get a rough understanding of the topic of the selected text;
do NOT make any assumptions about the text's intended use, only cover what was provided. Do NOT make assumptions about how or why the text was created.
If you cannot determine the topic, simply put: "Could not determine the topic."
If you cannot determine the tone, simply put: "Could not determine the tone.".
If you cannot identify any feelings, simply put: "Could not identify any feelings.".
Your introductory pragraph should start with: "Introduction: "

Second, scan the selected text for main ideas or key points. If the text already has bullet points, a numbered list, or a different sequential order, 
simplyfy and record only the significant points. label this section "Key Points/Main Ideas:".
Use as many bullet points as you need, but each of your bullet points should be no longer than 250 characters.
Present the selected key ideas in a numbered list, such as:
1. ....
2. ....
3. ....

so on and so forth. If there are no key points or main ideas, simply put: "Could not locate any key points."

Third, scan the selected text for any biases. If there are any biases estimate the level of biases on a scale of one to ten. One being the least, and ten being the greatest.
This should come at the very end.
Label this section "Bias (0-10):" and write a value 0 through 10.

```{text}```
"""

response = get_completion(prompt)

print(response)