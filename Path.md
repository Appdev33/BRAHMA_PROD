I am planning to create a windshield installation project with the following points in mind

TechStack - React 19 + Vite + Tailwind CSS 4
            BackEnd Python FastApi Uvicorn
            Database Postgres alembic for migrations and versioned and also some operation for seed data initial

RepoStructure - seperate repo both for frontEnd and Backend
Plan to create docker File also for both and one seperate repo just for docker in case we plan to use later(but keep option open) this is INFRA folder
Developemnet to be done using virtual environment
Logging for both front end and backend should be and strucutred deatiled and latencyp95 and latency99 required later so timed and detailed - in Future we plan to integrate monitoring

RBAC there are admin roles, user roles who get onboarded , and a role for multiple teams who do mainaintence and manual work(this should be flexible)
one team -- Verify report manually and then chooses to  approve/reject

Ratings should be given by user for each teamMember and overall
There is lot of PII information all that has to be strongly encrypted with salts and stored

Proper pagination should be present for requests wherever required
Notifications should be there with email for now but option later to extend for whatsapp and sms

STRICT SKILLS
Dont write unecessary long comments only precise and upto the point.
Follow strict DRY principle, KISS, SOLID and design patterns wherever possible
Dont write unnecessary code only what is require we dont want to clutter all ther records

STRICT RULES
New Agent chat per story ID. Do not pile work on a long thread.
Plan chat ≠ build. Build only in Agent mode with one ID.
TDD: fail the listed test file → smallest code → run only that file → stop. A second agent verifies with that same command
Each story must stand alone: AC, files, TDD path, verify command. No “do after X / slice with Y” unless the files truly cannot compile without it.
? / continue = resume the last step only; do not rediscover.
Dont clutter too many unecesay code and code files

USER STORIES:
Create User stories for each task such they are independent and can be independenlty taken by any agent, so each agent does not have to have a lot of context
For fast loopup we can store a map of only imp files and what they do in very short for quick lookup and changes
create each user story upto 1-8 points 
define User story precisely and consoisely , write tests before dev to validate US
avoid adding too much unecssary info in each US upto the point and precise
add code with proper api versioning also

FLOWS 

Customer Journey - Login/Signup/Profile/Vehicle

    A new user should create and register himself before he starts with an enquiry or Claim()
    A user can have multiple claim and vehicles but has only one primary vehicle which autofills when he logs in
    A user create his profile first by registring email password --> thorough jwt or email sent to user his account hi activated
    once 
    1) activate a new user fills 
        Senstive information and PII information should be ebcrypted strongly wbefore storing with salt
        a) Profile details
            Name, Email, Phone, Password, DOB, Aadhar, PAN, DL, Vehicle, Address (multiline), City, State, Pincode
        b) vehicle details one time step
            Vehicle Number (Number Plate), Chassis Number, Engine Number, RC (Image), Brand (e.g. Hyundai, Honda), Make (e.g. i10, i20), Year of Manufacturing, Fuel Type (Petrol, Diesel, CNG, Electric) 

    2) already existing user signs has a primary vehicle saved for his vehicle always which he has an option to change- we autofill as much info as possible for existing customers:
    Customer in his first screen sees following as shown in customer.jpg
   
    with 
    2. 
        a)Claims Summary Cards at top
        Metric	Current Value	Change	Comparison
        New Claims	42	↑ 12%	vs last week
        Documents Pending	28	↑ 5%	vs last week
        Assigned to Coordinators	36	↑ 18%	vs last week
        Survey Completed	19	↑ 27%	vs last week
        b) below this  summary of recent claims Paginated and at the end for each( claim details which opens in new page )
        CLM number V.     Vehicle Name	 Vehicle no	  Stage	         Created	
        CLM-2025-001      Activa        MH12AB9999	  Submitted      17/09/2026	   Details link( this show in details of this claim with flow or stage where it is in a new page)

      c) Option to create new claim/enquiry
           (start a new enquiry claim)
           Step1 profile info (auto fill with allow option to change)
                 Name, Email, Phone, Aadhar, PAN, DL, Vehicle Number, Address   
           
           Step2 
                a) vehicle info (auto fill with primary for each user allow option to change)
                    Registration Number (Number Plate),  Brand (e.g. Hyundai, Honda), Make (e.g. i10, i20), Year of Manufacturing, Fuel Type (Petrol, Diesel, CNG, Electric) -- radio button with options   
                
                b) below we add an option for payment types(choose one only)
                    Option	Description
                    Cash	Pay the full service amount directly. No insurance paperwork needed.
                    Insurance	Use your vehicle insurance for part of the cost. You may pay the remaining balance.
                    Cashless	Full insurance claim — upload policy and incident documents. Our team handles the insurer.
                c) if above chosen option is Insurance or casheless we open section to upload documnets:


                Upload Section --- only visible certain documents as per choice of cusomter during payment as cash. or (cashless) or isurance
                    for all user
                    RC (optional)No file chosen
                    Optional, max 10 MB

                    for insurance
                    Insurance policy (optional)No file chosen
                    Optional, max 10 MB

            
            Step3 is enquiry where we add:
                a carousel for windshiedl with following properties    
                Goal: Recreate wizard step “Select windshields” identically. Do not invent extra parts, extra slides, or multi front/back types.

                Carousel — features only (rebuild exact)

                3 slides wrap: Front → Back → Side
                Prev/next, n/3, pill jump
                Pill/photo Chosen · N = picks on that slide, not “viewing”
                Front: 1 of Sensor / Non-sensor / Don’t know
                Back: 1 of Plain / Heated / Don’t know
                Side: 0–4 doors (RF, RB, LF, LB)
                Keys: front:sensor|non_sensor|dont_know, back:plain|defogger_heated|dont_know, door:right_front|right_back|left_front|left_back
                New front/back pick replaces old on that part; door adds/toggles
                Chip tray: jump to slide, × remove
                Need ≥1 pick; never 2 fronts or 2 backs
                Radio vs checkbox cards + option info
                Same 3 PNGs; landing full-car image stays separate
            
            Step4 Details of Incident (incase of insurance or cashless)
                Time, Place, Damage Details, Narration, Parked/Moving, Driver Name, DL
                + Options to add images also

            Step5 - Add ons
                Add-ons — features only (rebuild exact)

                Wizard step, optional, 0–N picks
                Toggle only (no radio, no required)
                IDs locked: wiper | headlight | battery | taillight
                Labels: Wiper blades / Headlight restoration / Battery replacement / Taillight restoration
                Each row: checkbox look + label + info line
                Selected = primary border/fill; tap again = off
                Footer: “Skip if you don't need any add-ons.”
                Store string[] of those ids (empty OK)
                Do not add prices or extra add-ons unless a later story says so
            Step6 --- Coordinator review
                        all required documents and deatils submitted to Team1 for call and verification.
            Step7 --- Review and submit details
                      an option above to reviem and submit what all we have chose  
                      indicative price break down to user (decided by admin based on various steps to be decided)
                      based on insurance cashless or addons chosen by user this values changes
                      per case and above choices chosen
                      Here we can choose time slot and date(both drop down using calendar) as per customer prefernces which later the coordinator during manual verification can change also and admin has all
                    once coordinator calls and validates all documents from customer
            step8: validated Documents
                if valid user can start paymnet process through payment gateway (start with integration of free payment gateway but also option to  add multiple later)
                success or failed accordingly notify users




Co-ordinator Journey - Enquiry Validation
Co-ordinator  has two types of enquiries Submitted Enquires, Payment Done enquires
Submitted Enquires:
    This is a role that can be given by admin to multiple users
    all these users acan see submitted enquires and claims 
    They call customer and manually  
    - validates documents
    - validates info provided by cx during enquiry
    - checks stock availability / inventory management - manually only
    and if possible makes changes to any shceduling things(date timw after discussion)
    if enquiry is valid:
        mark it as valid and sent back to user for Payment
    if enquiry not valid:
        mark as invalid query with proper reasons and comments
        user can edit and make the corresponding changes    



Admin Journey and permissions:
    only admin should have permission for all roles creations
    admin should have view of all cases 
    admin has following visibility
        list of users
        list of enquiries
        list of co-ordinators (and other employees)
    admin task bar should following:
        DashBoard, CUstomers,Cordinators, vehicles, Settings, logout, option to collapse at end
    somethings like below can be visual aur admin.jpeg as shared:
    for the paginated summary of each claim with 
        Recent claims 
        Claim ID	Customer	Vehicle number Date	Status Assigned to 
    Above we should give option to search a claim or even filter based on  various stages   
    stepper flow
        Key UI Components Breakdown
        Header Section:
        Bold Claim ID (CLM-2025-00123) with a timestamp underneath.
        A status badge (Documents Pending) with a soft yellow/amber background.
        Vehicle Details Card:
        A rounded card container with a light background and subtle shadow.
        Car thumbnail image, vehicle name, registration number, model year, and insurance type.
        An action button ("View Vehicle & Policy Details") with an icon and right chevron.
        Claim Progress Stepper (Timeline):
        A vertical timeline connecting numbered steps with a vertical line.
        Completed/active steps use a filled green circle with a checkmark or number; pending steps use a grey outlined circle.
        Each step features a bold title, timestamp/status, and a short description text.



                
      










