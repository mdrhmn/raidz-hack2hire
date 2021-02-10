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

![alt text](https://imgur.com/Oeb5R9N)