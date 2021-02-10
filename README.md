# Team Raidz (Dell Hack2Hire)

## Introduction

This is the repository for our team (Raidz)'s first place award-winning Event Management System (EMS) web application for Dell Technologies Malaysia's Digital Virtual Hack2Hire on the 3-4 February 2021.

Team Raidz:
1. **Muhammad Rahiman bin Abdulmanab**
2. **Nur Faidz Hazirah binti Nor'Azman**

Our team managed to **tie in first place** alongside TryHarders team, the first time in the history of the Dell Hack2Hire event since its inception for a tie to happen. Both of us were also **shortlisted for the coveted grand prize** which is the **permanent job offer as IT Software Engineer** at Dell Technologies Malaysia, Cyberjaya.

<hr>

### What is Hack2Hire?

**Hack2Hire** is a holistic hiring process which allows to observe students on their problem solving skills, learnability, collaboration, empathy, team work and articulation. This is a great platform for students to have accelerated learnings and solve Industry problems which makes them more industry ready. It also helps in maturing the college & industry ecosystem and provides platform for collaboration & sharing ideas/best practices and industry transformation. 

Summary of Hack2Hire:
- 1 week of preparation
- 2-4 member per team
- 1 problem statement
- 2-day mass hiring event
- 12 hours of intense coding

<hr>

### Problem Statement

The **IT Development Program (ITDP)** is a 2-year global program for our recent full-time college hires. In the program, there are a variety of events such as social hangouts, trainings, volunteer opportunities, etc. 

The regional program managers have tried a variety of solutions to track the progress of participants in the program and post sign-ups for the types of events listed above. 

ITDPs (program participants) want to know their status in the program (trainings completed, events attended) and need an easy way to sign-up for new events. 

**Create a user-friendly solution that helps us address the needs of the IT Development Program PMs and participants.**

<hr>

### ITDP Personas

There are **3 types of ITDP personas/stakeholders** to consider:

1. **ITDP Participant**
- My name is John and I am a participant in the IT Development Program. 
- I currently work on the Buyers Experience space under Dell.com
- I do my required ITDP trainings
- I have a busy work schedule so I attend maybe 1 or 2 ITDP events a quarter sometimes none.
- I want to know how I am doing on my attendance in the program.

2. **ITDP Committee Lead**
- My name is Sally I am a participant in the IT Development Program and a committee lead.
- As a committee lead, I work with fellow ITDP participants on different events. 
- I haven’t completed all my trainings
- Because I plan a variety of events I attend most ITDP functions. 
- I want to know how many trainings I am away from attending summit. 

3. **ITDP Program Manager**
- I am Joyce, the ITDP program manager.
- I work with ITDP Committee Leads to plan trainings, social hangouts, and volunteer events. 
- Part of my role is identifying top talent in the program based off manager feedback and the ITDP participants level of engagement.
- I want a one stop shop view of every ITDPs level of engagement from training to event attendance.

<hr>

### Solutions

Due to time constraint and lack of manpower (we were among the smallest team there is), we strategised to implement features that covers all 3 personas centered around 1 use case: **Event Creation and Management**.

**List of Features:**
1. **ITDP Participant**
- View all available/active events 
- Register for events
- Receive registration email and SMS notification
- View details of registered events
- Edit event registration status 
- Submit feedback for attended/completed event

2. **ITDP Committee Lead**
- Create events
- View proposed events by Program Manager
- Edit event details

3. **ITDP Program Manager**
- Propose events to Committee Lead
- View details of all proposed events to Committee Lead
- View feedbacks from Participants
- View details of created events
- Auto-register/invitation of event participants (trainings)


## Technology Stack

### Front-end
* Bootstrap 4.5.2
* jQuery 3.5.1
* Popper.js 1.16.1
* Bootstrap-Select 1.13.14
* TailwindCSS 2.0
* Font Awesome 5.14.0
* DataTables 1.10.21
* Chart.js 2.8.0
* Summernote 0.8.18
* Moment.js 2.28.0
  
### Back-end

* Django==3.1.6
* twilio==6.51.1

### Database Design (ERD)

![Imgur Image](https://imgur.com/QLmrChM.png)

## Features

### Home/Landing Page

For the home or landing page, we derive and copy similar design from existing [Dell Technologies website](https://www.delltechnologies.com/en-my/index.htm). Upon advice and recommendation by our mentor Mufhim Anees, we also borrowed several design elements from [Dell's own Design System](https://www.delldesignsystem.com) such as the font type (Roboto) and font size.

Replicating existing Dell website design maintains similar look and feel to **ensure users will adapt quickly to the web app**, in line with the web app's goal to be closely integrated to Dell's existing ecosystem. Reusing components is also an efficient approach to save precious time in drafting the UI/UX of the web app.

Users regardless of role/persona and log in status will be met with the home or landing page by default.

![Imgur Image](https://imgur.com/Oeb5R9N.png)

<hr>

### Log In Page

The log in page has a simple, minimalistic UI design where users can enter their email and password, which is the preferred authentication combination based on our requirements gathering with the stakeholders. Users also have the ability to show/hide their password.

The main highlight of this feature is that users do not have to worry about manual role selection during log in, as the server-side processing will auto detect the user's role upon logging in. All users will be redirected to the home/landing page after successful log in.

![Imgur Image](https://imgur.com/77UD1dM.png)

<hr>


### Event Menu/Registration Section

The event menu/registration section is consolidated together with the home/landing page to minimise clicking and page redirection (less hassle). The design approach is based upon [Udemy's website](https://www.udemy.com/courses/development/web-development/). The event menu/registration section is divided into 2 subsections: **Currently Active Events** and **Register for ITDP Events**.

1. **Currently Active Events**

    For this section, users will be able to **see the top 4 active events in card form** from all categories (Social Hangout, Training, Volunteering, Summit). Hovering through each card will show a Bootstrap popover consisting of the event details. Participants can register for the events by clicking the Register button. For our prototype, the events displayed in the photo below are merely placeholders.'

    ![Imgur Image](https://imgur.com/oF9Mn2K.png)

2. **Register for ITDP Events**

    This section will **list down all active (read: registrable) ITDP events in card form**. Each card will show the event category, title, description and registration due datetime. Participants can register by clicking the Register button, which will pop up a confirmation modal. Because most of the user information regarding the registration is derived from the User model, participants no longer have to fill in a new and separate registration form. Participants will be redirected to the Event Management page after successful registration.

    Participants also have the ability to **filter ITDP events based on category** via the left-hand-side panel. 

    ![Imgur Image](https://imgur.com/eaJ2Lrp.png)


<hr>

### Event Management Page (Participant)

The Event Management page for participants **shows the list of registered events in a table format**. Using DataTables package, the table allows users to sort and search entries. The table shows the event name and category, registration due datetime, status and feedback.

![Imgur Image](https://imgur.com/FpJD8Fm.png)

When the registration status is Registered, participants are able to **change the status to Unregistered** by clicking the Edit icon beside the status. This will prompt a modal for users to select the desired status. The Submit Feedback button is also disabled (greyed out) as participants are not allowed to submit any feedbacks prior to event completion.

![Imgur Image](https://imgur.com/CpNYsLp.png)

When the registration status is Attended (meaning event is complete and user attended the event), the Submit Feedback button is enabled and participants can **submit/edit feedback** by clicking the button. A modal will appear which allows participants to input the written feedback.

![Imgur Image](https://imgur.com/tPnKOcw.png)

<hr>

### Event Proposal Page (Committee Lead)

For Committee Lead and Program Manager, they have a **separate administrator-like page** for them to manage events which are accessible via the navigation bar link at the home/landing page. 

The Event Proposal page for committee leads allows them to **view list of proposals filed by the Program Manager** in table format (DataTables).

![Imgur Image](https://imgur.com/1wwOLvx.png)

<hr>

### Event Management Page (Committee Lead)

Committee Lead is considered a subset of Participant (can be both participants and organisers of events). The Committee Lead's Event Management page is different from that of Participant's as it allows committee leads to **create new events**, **edit existing events** as well as **see details of all events organised** by the committee lead.

![Imgur Image](https://imgur.com/MTGfkYN.png)

To create a new event, committee leads can click the Create New Event button to pop up a modal form shown below:

![Imgur Image](https://imgur.com/Mq95KBo.png)

To edit an existing event, committee leads can click the Edit button under the Edit Event column in the table to pop up a modal form shown below:

![Imgur Image](https://imgur.com/D3IKKmu.png)

<hr>

### Event Proposal Page (Program Manager)

One of the roles of Program Manager in terms of event creation flow/use case is to first propose ITDP events for the quarter to the assigned Committee lead. This can be done through the Event Proposal page for the Program Manager. 

![Imgur Image](https://imgur.com/OYEL6ry.png)

The Program Manager can **propose a new event** by clicking the Propose New Event button. This will prompt a modal form for the Program Manager to fill in.

![Imgur Image](https://imgur.com/CYXDQEv.png)

<hr>

### Event Registration Page (Program Manager)

This Event Registration page allows the Program Manager to **issue event registrations to ITDP participants** for specific event. This feature is useful for events such as trainings, which are compulsory for participants to attend and meet a certain quota. Program Managers can select the event as well as multiple participants to send the RSVP invitation. All registered participants will receive email and SMS notifications.

![Imgur Image](https://imgur.com/LE2OuNt.png)

<hr>

### Event Management Page (Program Manager)

The Event Management page for Program Managers is essentially the same as Committee Lead's, with the slight change that Program Managers will be able to see all events organised instead of ones organised/proposed by them.

![Imgur Image](https://imgur.com/R96Y26a.png)

<hr>

### Feedback Management Page (Program Manager)

The last feature allows Program Managers to view the list of feedbacks for each participant. The feedback entry will be automatically created upon event registration.

![Imgur Image](https://imgur.com/uuEYJnp.png)
