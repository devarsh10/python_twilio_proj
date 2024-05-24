# python_twilio_proj
This project will send you DevOps Tasks every day.

# Implementation
1. First of All, the structure of the Database is in JSON (JavaScript Object Notation) which looks something like this.

![image](https://github.com/devarsh10/python_twilio_proj/assets/83413047/63b8850c-02de-4953-a6de-13c4c9209806)

2. Now, the flow of code is something like,
   - Here, first, we'll declare the variables using the "expose". So that we do not need to use the hardcore values which will increase the Security.

![image](https://github.com/devarsh10/python_twilio_proj/assets/83413047/c74ad8bf-2472-44f1-bf32-1ad85b42f364)

**Till now we're done with configuring the static database and variables we're going to use.**

3. Now, let's talk about twilio_prac.py file. In this file, the question will be selected from the running JSON server and the function send_whatsapp_text will trigger the function in the twilio_conn file.

4. Now how the Question will be sent?
   - Using Cron-job, in the cron.py file.
   - We're using apscheduler to set the timezone and time.
   - Lastly, setting the time when we want the message. That's it.
