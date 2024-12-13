from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample topics and posts for the discussion board
topics = {
    "Historical Roots of Education": [
        {
            "author": "Alex",
            "content": "It's fascinating, yet troubling, how redlining in early American history has impacted education systems. Schools in redlined districts received far less funding, creating a disparity that persists even today. What do you all think about how this continues to affect us?"
        },
        {
            "author": "Jamie",
            "content": "Alex, you bring up an important point. The financial disparities rooted in redlining didn't just affect schools—they shaped entire communities. Poorly funded schools led to fewer opportunities for upward mobility. How do we even begin to address such a deeply rooted issue?"
        },
        {
            "author": "Taylor",
            "content": "One starting point might be equitable funding reform. But I think it goes beyond just money. Schools in underserved areas often lack access to experienced teachers and advanced resources. Shouldn't we also be addressing teacher placement policies?"
        },
        {
            "author": "Jordan",
            "content": "Taylor, I agree. But even when teachers are placed in these areas, burnout is a major issue because they're not given the support they need. We need systemic changes that go beyond just the schools—like tackling housing policies and healthcare access."
        },
        {
            "author": "Alex",
            "content": "You're right, Jordan. The interconnectedness of these issues is overwhelming. And let's not forget how redlining and segregation have also fueled racial tensions, which have erupted into riots. Do you think educational reform could actually play a role in reducing such tensions?"
        },
        {
            "author": "Jamie",
            "content": "It could, Alex. But it would require a cultural shift as well. Education has to become more inclusive—not just in terms of resources, but in curriculum. How often do students learn about systemic racism and its impacts in a meaningful way?"
        },
        {
            "author": "Taylor",
            "content": "Good point, Jamie. Representation in education is so important. When students see their history and struggles acknowledged, it fosters a sense of belonging. But how do we convince policymakers to prioritize this?"
        },
        {
            "author": "Jordan",
            "content": "Maybe by showing them the data. Schools with inclusive curriculums often report lower dropout rates and higher student engagement. It's a win-win. But again, it takes funding and political will."
        },
        {
            "author": "Alex",
            "content": "So true, Jordan. And we also need to address implicit biases in teachers themselves. If educators aren't equipped to handle discussions on race and inequality, we're just perpetuating the problem."
        },
        {
            "author": "Jamie",
            "content": "Training for teachers on these issues is crucial, Alex. But what about the students? How do we engage them in these conversations without alienating anyone?"
        },
        {
            "author": "Taylor",
            "content": "I think it starts with fostering open dialogue. Safe spaces for discussion can go a long way. But it has to be genuine and not performative, or students will see right through it."
        },
        {
            "author": "Jordan",
            "content": "Absolutely, Taylor. And student-led initiatives can be powerful too. When students take the lead on addressing these issues, it resonates more with their peers."
        },
        {
            "author": "Alex",
            "content": "Student-led initiatives are great, but they need support from teachers and administrators. Otherwise, they're just fighting an uphill battle."
        },
        {
            "author": "Jamie",
            "content": "And that's where community involvement comes in. If parents and local leaders are engaged, it adds weight to the movement."
        },
        {
            "author": "Taylor",
            "content": "Exactly. It's a cycle. Schools impact communities, and communities impact schools. Breaking the cycle of inequity requires both to work together."
        },
        {
            "author": "Jordan",
            "content": "It's a massive undertaking, but conversations like this are a good starting point. Awareness is the first step toward change."
        },
        {
            "author": "Riley",
            "content": "One thing we haven't touched on is how modern zoning laws still mirror historical redlining practices. Even today, schools are often funded based on local property taxes, which directly ties their resources to the wealth of their neighborhoods. How do we untangle this web?"
        },
        {
            "author": "Alex",
            "content": "Great point, Riley. Reforming funding models might be the key. What if state or federal governments played a larger role in equalizing school budgets, rather than leaving it to local taxes?"
        },
        {
            "author": "Jamie",
            "content": "It's an idea worth exploring, Alex. But how do we ensure that increased funding actually translates into better outcomes for students? Maybe we need accountability measures to track how schools use their resources."
        },
        {
            "author": "Taylor",
            "content": "Accountability is crucial, Jamie. But we also have to trust educators to know what their schools need most. A balance between oversight and autonomy could make a big difference."
        }
    ],
    "Technology in Education": [
        {
            "author": "Jordan",
            "content": "The landscape of education has dramatically shifted in recent years with the rapid incorporation of technology. One of the most transformative forces in modern education is generative artificial intelligence (AI), such as ChatGPT. These AI tools are now being used in classrooms across the world, providing personalized learning experiences, assisting teachers in grading and lesson planning, and offering students immediate access to a vast array of resources. However, as exciting as this new era of technology is, it also comes with complex challenges that we must confront to ensure that technology benefits all students equally and effectively."
        },
        {
            "author": "Taylor",
            "content": "Generative AI, like ChatGPT, has the potential to enhance learning by offering instant assistance, personalized feedback, and engaging educational content. For example, students can interact with AI to ask questions about homework, receive tutoring in various subjects, or even generate creative writing prompts. Teachers can use AI to automate administrative tasks, analyze student progress in real-time, and identify areas where individual students may need additional support. The possibilities for improving the learning experience seem endless. AI can transform traditional education models into more flexible, adaptive systems that cater to the unique needs of each student."
        },
        {
            "author": "Jordan",
            "content": "However, there are critical challenges to consider. One of the most pressing issues in the implementation of AI in education is the digital divide—the gap between students who have access to advanced technology and those who do not. While generative AI tools are becoming more sophisticated, the reality is that many schools, especially those in underfunded or rural areas, do not have the infrastructure to support such technologies. The lack of reliable internet access, insufficient devices for students, and undertrained educators are barriers that make it difficult to take full advantage of AI's capabilities. In fact, research has shown that students from low-income backgrounds are often the least likely to have access to the technology they need, further exacerbating inequalities in educational opportunities."
        },
        {
            "author": "Taylor",
            "content": "The digital divide extends beyond just hardware and internet access—it also includes disparities in digital literacy. Students in wealthier districts are more likely to be taught how to use advanced technology and digital tools from an early age, while those in underserved areas may never have the opportunity to gain these skills. Without equitable access to digital literacy programs, the gap between students who can harness the power of AI and those who cannot will continue to widen, perpetuating existing inequalities in education."
        },
        {
            "author": "Jordan",
            "content": "Furthermore, the adoption of AI in education introduces several ethical concerns. When AI tools like ChatGPT are implemented in classrooms, they can inadvertently perpetuate biases present in their training data. For example, if the data used to train these models contains biases based on race, gender, or socio-economic status, the AI could inadvertently reinforce these biases when interacting with students. This could manifest in AI tutoring systems providing biased feedback or in automated grading systems unfairly penalizing certain student demographics. To address this, it's essential that educators and policymakers prioritize fairness and transparency in AI tools used for education, ensuring that these systems are continuously evaluated for potential biases and that corrective measures are taken when necessary."
        },
        {
            "author": "Sam",
            "content": "Another issue is the lack of robust analytical testing for many AI systems deployed in schools. While AI tools may be widely adopted, there is often insufficient testing to evaluate their long-term impact on students' learning outcomes. Many educational technologies are introduced without rigorous analysis of their effectiveness. Without careful, evidence-based evaluation, we risk implementing systems that may not deliver on their promises—or worse, have unintended negative consequences. For instance, a study might reveal that AI-driven homework assistance tools are not as effective for struggling students as they are for those already performing well, leading to a widening achievement gap. Or, AI tools might not align with specific state standards, leading to disjointed educational experiences for students across different regions."
        },
        {
            "author": "Jordan",
            "content": "Teachers, while being the main facilitators of learning, may also face challenges when integrating AI into their classrooms. Without adequate training and support, educators might struggle to understand how to use AI effectively, let alone address the ethical and pedagogical issues it raises. The implementation of AI cannot simply be about providing tools; there must also be a concerted effort to provide professional development for teachers, equipping them with the skills to navigate the complexities of AI and use it in ways that complement their teaching methods and foster student success."
        },
        {
            "author": "Taylor",
            "content": "In addition, we must ask ourselves: how should AI be integrated into the classroom without replacing the essential human element? AI, while capable of personalized feedback, cannot replace the empathetic, creative, and relational qualities of a teacher. AI tools can transform learning, but the best use might be as a tool that empowers teachers rather than replaces them—helping educators with administrative tasks, supporting differentiated instruction, and providing additional resources for students. The key is to find a balance that maximizes the benefits of AI while still keeping human interaction at the center of the learning process."
        },
        {
            "author": "Jordan",
            "content": "Moreover, the shift toward AI-driven education raises questions about data privacy. AI tools often rely on large amounts of student data to personalize learning. This data may include sensitive information such as academic performance, learning preferences, and even behavioral data. If not properly protected, this data could be exposed to misuse or exploitation. Policymakers must establish strong regulations to protect student privacy while ensuring that AI systems are transparent in how they collect, store, and utilize this data."
        },
        {
            "author": "Taylor",
            "content": "In conclusion, while the integration of technology, particularly AI, into education holds great promise, it must be done thoughtfully and equitably. We need to ensure that all students, regardless of their socio-economic background, have access to the tools and resources necessary for success in a digital world. We must address the digital divide, train educators effectively, and subject AI systems to rigorous testing and evaluation to ensure their impact is both positive and fair. Only then can we unlock the true potential of technology in education, creating a system that benefits all learners and prepares them for the challenges of the future."
        },
        {
            "author": "Riley",
            "content": "One question to ponder: How do we ensure that teachers feel empowered, not overwhelmed, by the introduction of AI tools? Do we need AI-specific roles in schools to support educators?"
        },
        {
            "author": "Sam",
            "content": "Interesting thought, Riley. AI specialists in schools could help bridge the gap, providing both technical support and strategic advice on integrating these tools effectively."
        },
        {
            "author": "Taylor",
            "content": "That's a great suggestion, Sam. A dedicated AI coordinator could ensure that the tools align with educational goals and also address ethical concerns as they arise."
        }
    ],
    "Finding Passion Through Education": [
        {"author": "Sam", "content": "My passion for coding started with a teacher who encouraged me to join a robotics club. How can we create more opportunities like this for students?"},
        {"author": "Riley", "content": "That's inspiring, Sam! I think mentorship programs could help. Pairing students with professionals in various fields might spark interests they never considered."},
        {"author": "Sam", "content": "Absolutely, Riley. Mentorship could also guide students through challenges and help them see the practical applications of what they learn in school."},
        {"author": "Riley", "content": "And it could build confidence too. When students see someone like them succeeding, it reinforces the belief that they can achieve their goals."},
        {"author": "Jordan", "content": "I completely agree with both of you. Giving students real-world experiences makes a big difference. How do we convince schools to invest in these types of programs?"}, 
        {"author": "Taylor", "content": "It might help to present data that shows how engagement in hands-on learning activities leads to higher academic success."},
        {"author": "Jordan", "content": "Yeah, showing the correlation between passion-driven learning and student performance could make a compelling case."},
        {"author": "Riley", "content": "I also think we should incorporate more career exploration into the curriculum. Not all students know what's out there beyond high school."},
        {"author": "Sam", "content": "Definitely. Exposing students to a variety of fields and industries would help them understand the vast possibilities they can pursue."},
        {"author": "Taylor", "content": "What about creating 'passion projects'? Let students choose topics they care about and spend time developing them."},
        {"author": "Jordan", "content": "I love that idea. It could help students feel more ownership of their learning."},
        {"author": "Riley", "content": "Yes! And we could encourage them to collaborate on projects. Working together can spark even more creativity."},
        {"author": "Taylor", "content": "Exactly. Sometimes students don't realize their own potential until they collaborate with others who share similar interests."},
        {"author": "Sam", "content": "It's also essential to create a culture where failure is seen as part of the learning process, not something to be afraid of."},
        {"author": "Riley", "content": "I couldn't agree more, Sam. When students feel safe to fail, they can take risks and experiment with new ideas."},
        {"author": "Jordan", "content": "Building resilience through failure is key. How can we integrate this mindset into the curriculum?"}, 
        {"author": "Taylor", "content": "We could use project-based learning. It allows students to work through challenges in real-time, fostering problem-solving and resilience."},
        {"author": "Sam", "content": "Project-based learning could be the perfect way to engage students, especially in technical subjects like engineering."},
        {"author": "Riley", "content": "Imagine a world where students can explore passions without the pressure of standardized tests. I think we'd see a more motivated generation."},
        {"author": "Jordan", "content": "Yes! Focusing on passion projects might make education feel less like a series of hoops to jump through."},
        {"author": "Taylor", "content": "What if we redefined success? Maybe it's not just about grades, but about whether a student discovered something they care about."},
        {"author": "Sam", "content": "That's a powerful shift. When passion drives learning, the outcomes are often greater than we expect."},
        {"author": "Riley", "content": "And those students may end up making significant contributions to their communities in the future."},
        {"author": "Jordan", "content": "Exactly. The key is helping students connect what they're learning to the world around them."},
        {"author": "Taylor", "content": "Agreed. It's about relevance. When students see how their education aligns with their interests and the real world, their engagement skyrockets."},
        {"author": "Sam", "content": "What do you think about bringing in industry professionals as guest speakers? It could help bridge the gap between classroom learning and real-world experience."},
        {"author": "Riley", "content": "I think that's a great idea, Sam! It would bring fresh perspectives and help students see the direct impact of their studies."},
        {"author": "Jordan", "content": "Absolutely. It would make learning feel more purposeful, especially for students who aren't sure what they want to do yet."},
        {"author": "Taylor", "content": "I agree. Let's focus on passion-driven education to create a generation of innovators and lifelong learners."}
    ],
    "Cultural Competence in Education": [
        {
            "author": "Sam",
            "content": "Building on what Taylor mentioned earlier, we also need to integrate experiential learning opportunities that expose students to different cultures. This could include exchange programs, partnerships with schools in other countries, or even virtual cultural exchanges. Experiencing diversity firsthand can be a powerful teacher."
        },
        {
            "author": "Alex",
            "content": "That's a fantastic idea, Sam. Another approach might be incorporating storytelling as a method to build cultural competence. Inviting community members to share their experiences or incorporating students' family histories into projects can make the lessons more personal and impactful."
        },
        {
            "author": "Jordan",
            "content": "I love that, Alex. Storytelling not only educates but also fosters empathy. When students hear about the lived experiences of others, it humanizes abstract concepts like discrimination or privilege. It could also be a way to build connections among students."
        },
        {
            "author": "Riley",
            "content": "To add to that, there should also be an emphasis on challenging stereotypes. Lessons could include discussions about implicit biases and how they manifest in our daily interactions. This might be uncomfortable, but it's essential for creating truly inclusive environments."
        },
        {
            "author": "Jamie",
            "content": "Riley, I completely agree. But these discussions must be facilitated with care. Schools need trained professionals to lead these conversations to ensure they're productive and don't inadvertently reinforce biases."
        },
        {
            "author": "Taylor",
            "content": "And let's not forget the role of arts and media. Films, music, and literature from diverse cultures can be powerful tools for education. By integrating these into the curriculum, we can make learning about different cultures engaging and relatable."
        },
        {
            "author": "Alex",
            "content": "Yes, Taylor! Art has a unique way of breaking down barriers and creating shared understanding. Schools could even host cultural festivals or art showcases where students present work inspired by their heritage or learn about others' traditions."
        },
        {
            "author": "Sam",
            "content": "Cultural festivals are a great idea, Alex. They could also include workshops where students learn new skills, like cooking dishes from different cultures or practicing traditional dances. These hands-on activities make learning immersive and memorable."
        },
        {
            "author": "Jordan",
            "content": "But while these events are great, we need to ensure they're not just one-off celebrations. The message of inclusivity and respect must be woven into the fabric of daily school life."
        },
        {
            "author": "Riley",
            "content": "Absolutely, Jordan. Inclusive practices should extend to everything, from classroom seating arrangements to the language used in school policies. It's about creating an environment where diversity is not just tolerated but celebrated."
        }
    ],
    "Mental Health Support in Schools": [
        {
            "author": "Taylor",
            "content": "One critical piece is ensuring that mental health education starts early. Even in elementary school, students can learn age-appropriate concepts about emotions and coping mechanisms. Early intervention is key to building resilience before challenges escalate."
        },
        {
            "author": "Jamie",
            "content": "Taylor, that's such an important point. And for older students, schools should offer elective courses on mental health, psychology, or wellness. These could not only provide knowledge but also spark interest in mental health careers."
        },
        {
            "author": "Alex",
            "content": "To Jamie's point, involving students in creating these courses could be beneficial. Peer-to-peer education can be powerful, especially when students feel like they're learning from someone who truly understands their struggles."
        },
        {
            "author": "Sam",
            "content": "Yes, and peer support groups can also help reduce stigma. Students may feel more comfortable opening up to their peers than to adults. Training student leaders in mental health first aid could make these groups even more effective."
        },
        {
            "author": "Jordan",
            "content": "That's a great idea, Sam. But peer support shouldn't replace professional resources. Schools need to prioritize hiring licensed counselors and therapists. We need to stop seeing mental health services as a luxury and start treating them as a necessity."
        },
        {
            "author": "Riley",
            "content": "Agreed, Jordan. Another thing schools could do is provide resources for families. Many students face mental health challenges that stem from or are exacerbated by home environments. Workshops or counseling for parents could help address issues holistically."
        },
        {
            "author": "Taylor",
            "content": "And for students who are hesitant to seek help, anonymous options could be a lifeline. Online platforms or mental health hotlines could provide immediate support without fear of judgment."
        },
        {
            "author": "Jamie",
            "content": "Taylor, I like the idea of anonymity. Schools could also implement wellness check-ins, where every student has the opportunity to speak with a counselor regularly, even if just briefly. This normalizes seeking help and makes it accessible."
        },
        {
            "author": "Alex",
            "content": "That's a great suggestion, Jamie. Another approach might be integrating mental health into physical education. Activities like yoga or guided relaxation could be part of PE classes, combining physical and mental well-being."
        },
        {
            "author": "Sam",
            "content": "Mindfulness and meditation could also be introduced as part of daily routines, like a short session at the start of each day. These practices have been shown to reduce stress and improve focus among students."
        },
        {
            "author": "Jordan",
            "content": "But to implement all these ideas, schools need proper funding. Advocating for increased budgets and grants for mental health initiatives should be a priority for education policymakers."
        },
        {
            "author": "Riley",
            "content": "True, but advocacy needs to come from all sides. Parents, students, and educators need to work together to make mental health support a clear priority. Community partnerships can also play a role in lobbying for change."
        },
        {
            "author": "Taylor",
            "content": "And once funding is secured, schools must ensure it's used effectively. Regular evaluations of mental health programs can help identify what's working and what needs improvement."
        },
        {
            "author": "Jamie",
            "content": "Exactly, Taylor. Transparency is essential. Sharing the outcomes of these evaluations with the school community can build trust and encourage ongoing support for mental health initiatives."
        },
        {
            "author": "Alex",
            "content": "In the end, addressing mental health is about creating a culture of care. When students feel supported, they're more likely to succeed academically and personally. Schools should strive to be safe spaces for all students."
        },
        {
            "author": "Sam",
            "content": "Well said, Alex. Mental health isn't just an individual issue—it's a community one. By fostering a supportive environment, schools can help build a generation that values empathy and well-being."
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html', topics=topics)

@app.route('/topic/<topic_name>', methods=['GET', 'POST'])
def topic(topic_name):
    if topic_name not in topics:
        return "Topic not found", 404

    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        topics[topic_name].append({"author": author, "content": content})

    return render_template('topic.html', topic_name=topic_name, posts=topics[topic_name])

@app.route('/new_topic', methods=['GET', 'POST'])
def new_topic():
    if request.method == 'POST':
        topic_name = request.form['topic_name']
        if topic_name and topic_name not in topics:
            topics[topic_name] = []
            return redirect(url_for('home'))

    return render_template('new_topic.html')

if __name__ == '__main__':
    app.run(debug=True)
