# import regular expression
import re

message = '''
Email: adebayoajagunna@gmail.com | 250 E 29TH street, apt 2c, Brooklyn NY 11226 | cell: 917-900-2051 ,  917-902-2051

EDUCATION
CUNY, The City College of New York, New York, NY

Bachelor of Science degree in Computer Science, August 2019 – Present

CUNY, Borough of Manhattan Community College (BMCC), New York, NY

Associate of Science degree, Honors in Computer Science, August 2015 – May 2018
•	GPA: 3.953
•	Dean’s List: January 2016 – May 2018

RELEVANT COURSE WORK
•	Calculus I, II, III, Probability and Statistics for computer science
•	Data Structures in Java, Introduction to Java, Algorithms, Introduction to Python
•	Assembly Language and Architecture, Discrete Structures

COMPUTER SKILLS
•	Languages: Java, JavaScript, HTML5/CSS3, Python, Nodejs, React, Swift, C++

•	Systems: Windows, Mac OS, Linux
•	Frameworks/Tools: Terminal, Git, GitHub, JetBrains IDE’s, Bracket, Visual Studio, Heroku

SPECIAL PROJECTS
Lehman College NSBE(Nation Society of Black Engineers) Hackathon, November 2019
•	Created a mobile application using React-Native called MONYC, November 2019
•	Created a sign-in page that handles user’s authentication, November 2019
•	Created a maps page that displays a map of all locations of MONYC, November 2019
•	Contributed to the user’s profile page, November 2019
•	Ensured the app was capable of basic functionality, November 2019
•	Ensured all team members where actively working on designated task for the app, November 2019

100 Days of Code (classes taken on Udemy), June 2018 – September 2018
•	Created basic website using HTML, CSS, and JavaScript, May 2018
•	Created a countdown application using Nodejs
•	Created a recipe shopping website using React and Redux, May 2018

•	Created a chat application using socket IO, HTML and Node.js, July 2018

•	Deplored created website using Heroku and Git, August 2018

AWARDS

•	Top 6 Finalist, Lehman College NSBE Hackathon, November 2019
•	Winner of Capital One Best Financial Hack, Lehman College NSBE Hackathon, November 2019
•	Fourth place, , Lehman College NSBE Hackathon, November 2019
•	Achievers Award, maintain 4.0 G.PA, BMCC ,August 2015 – January 2018

SCHOLARSHIPS/MEMBERSHIP

•	Member, Phi Theta Kappa, September 2016 – May 2018
•	Member, Phi Theta Kappa, September 2016 – May 2018

•	BMCC Foundation Scholarship Recipient, September 2016 – May 2018

•	BMCC Achiever’s Award for 4.0 GPA, September 2016 – December 2017



WORK EXPERIENCE
Urban Male Leadership Academy (BMCC), New York, NY

Tutor and Ambassador, February 2016 – December 2018
•	Served as a tutor for students in computer science and mathematics
•	Assisted in planning trips and events for members of the club

VOLUNTEER ACTIVITIES
Computer Programming Club (BMCC), New York, NY
Treasurer, August 2017 – May 2018
•	Prepared the club’s budget and provided financial reports on a bi-weekly basis
•	Organized hour of code and mini on campus hackathons
•	Organized and taught coding workshops for web programming using HTML and CSS

Brooklyn Chamber of Commerce, New York, NY
Go! Digital Service Corps Member, September 2016 – April 2017
•	Created business pages for small business owners using Google My business
•	Updated business information on Google pages for small business owners
•	Monitored changes in business monthly.
•	Recorded business changes such as how many times the business was visited monthly using Excel
times the business page has been visited
'''


phoneNumber = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

# Matched Object

mo = phoneNumber.findall(message)
print(mo)
