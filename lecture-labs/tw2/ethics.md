# Matt Hudson - Tuesday Week 2 Lab - CS4320 Fall '19

Ethical Considerations in Software Engineering

## 1. Software developers should consider the scale of their work.

When building software applications, they can be small-scale (i.e. just a personal project to help oneself or close friends) all the way to large-scale applications that are used by or affect millions (or even billions!) of people (such as developing Google's landing page or software that manages Social Security information for the US). Dropping a table in a local database for a school project is not nearly as much damage as dropping a live production database for a company's application. Developers need to make sure that changes to large-scale projects are made smartly, as bugs or critical errors can affect millions of people. 

## 2. Software developers should consider the impact of their work.

If a bug in my software causes a miscalculation in my indie first person shooter game so a gun does twice the damage it should, it's frustrating, but doesn't harm anyone (12 year old Call of Duty players would disagree). That same miscalculation, if the software is running on a NASA spacecraft, or the stock market, or... you get the idea. It could do serious damage: the spacecraft's engines could burn twice as long, or twice as many shares get sold as they should be, etc. Software engineers are often trusted with critical systems that could seriously affect the world if they fail or have unintended consequences. People's lives could even be lost because of a software bug (this extends to other disciplines of engineering).

## 3. Software developers should develop openly with their peers.

Software documentation plays a role not only in how other develoeprs understand *why* particular decisions were made during development, but also clients and/or other interested parties (for example, I interned with Cerner, and they can be audited by government agencies). The main idea behind peer collaboration is to provide 'checks and balances' on a multi-person project. Developing great documentation allows others to understand why you did something the way you did, and also for them to identify problems that could arise as a result of that decision. Not being open with peers hinders improvement and could even result in malicious code being sneaked into software (i.e. a backdoor into a database).
