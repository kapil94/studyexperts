from flask import Flask,render_template,url_for,redirect,Response,jsonify
import boto3
import os




app=Flask(__name__)

BUCKET_NAME = 'testproject2'


@app.route('/')
def index():
	return render_template("index.html")

@app.errorhandler(Exception)
def exception_handler(error):
	return "!!!!"  + repr(error)
	
@app.route('/Syllabus/class 10/<string:chapter_name>')
def syllabus_class_10(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if chapter_name=="English":
		key="Syllabus/class 10/English.pdf"
	
	elif chapter_name=="sst":
		key="Syllabus/class 10/sst.pdf"
	
	
		
	file_obj=my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	
	
@app.route('/Syllabus/class 10')
def Syllabus_class_10():
	return render_template("Syllabus_class_10.html")
	
@app.route('/Syllabus/class 12')
def Syllabus_class_12():
	return render_template("Syllabus_class_12.html")
	
@app.route('/Syllabus/class 12/<string:chapter_name>')
def syllabus_class_12(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if chapter_name=="English":
		key="Syllabus/class 12/CLASS XII ENGLISH CORE.pdf"
	
	elif chapter_name=="Geography":
		key="Syllabus/class 12/GEOGRAPHY CLASS 12.pdf"
	
	elif chapter_name=="History":
		key="Syllabus/class 12/History Class XII.pdf"
		
	elif chapter_name=="Economics":
		key="Syllabus/class 12/ECONOMICS CLASS XII.pdf"
		
	elif chapter_name=="polsc":
		key="Syllabus/class 12/polsc.pdf"
		
	file_obj=my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

############################### Political Science #####################################################
@app.route('/Polscience/class 10')
def polX():
	return render_template("PoliticalScienceX.html")

@app.route('/PoliticalScience/Class10/Studynotes')
def polnotes():
	return render_template("PoliticalScStudynotes.html")

@app.route('/PoliticalScience/Class10/<string:chapter_name>')
def politicalnotes(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if chapter_name == "federalism":
		key = "politicalsc/class 10 notes political science/federalism notes.pdf"
	
	elif chapter_name=="Powersharing":
		key = "politicalsc/class 10 notes political science/ch-1 notes.pdf"

	elif chapter_name == "Democracy":
		key = "politicalsc/class 10 notes political science/NOTES CH-3 CIVICS.pdf"
	
	elif chapter_name == "Outcomes":
		key = "politicalsc/class 10 notes political science/OUTCOMES OF DEMOCRACY NOTES.pdf"	
	
	elif chapter_name=="Parties":
		key ="politicalsc/class 10 notes political science/political parties notes.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	
	


@app.route('/PoliticalScience/Class10/<string:questions>/questions')
def PoliticalImp(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "federalism":
		key = "politicalsc/class 10 political science important questions/federalism important questions.pdf"
	
	elif questions=="powersharing":
		key = "politicalsc/class 10 political science important questions/important questions of power sharing.pdf"

	
	elif questions == "outcomes":
		key = "politicalsc/class 10 political science important questions/outcomes of democracy important questions.pdf"	
	
	elif questions=="political":
		key ="politicalsc/class 10 political science important questions/political parties important questions.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	
@app.route('/PoliticalScience/class12')
def polXII():
	return render_template("PoliticalScienceXII.html")	


@app.route('/politicalsc/important questions')
def polimp():
	return render_template("pol-imp.html")

@app.route('/polprev')
def polprev():
	return render_template("pol-prev.html")

@app.route('/politicalsc/previousyear/<int:year>')
def previousyr(year):
	
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	if year == 2015:
		key = "politicalsc/sst previous years/2015.pdf"
	
	elif year == 2016:
		key= "politicalsc/sst previous years/2016.pdf"
	
	elif year == 2017:
		key= "politicalsc/sst previous years/2017.pdf"

	elif year == 2018:
		key= "politicalsc/sst previous years/2018.pdf"
	
	elif year == 2019:
		key= "politicalsc/sst previous years/2019.pdf"
	
	elif year == 2020:
		key= "politicalsc/sst previous years/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/politicalsc/previousyear12/<int:year>')
def previousyr12(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "politicalsc/Previous_year_12/previous years 2015.pdf"
	
	elif year == 2016:
		key= "politicalsc/Previous_year_12/previous years 2016.pdf"
	
	elif year == 2017:
		key= "politicalsc/Previous_year_12/previous years 2017.pdf"

	elif year == 2018:
		key= "politicalsc/Previous_year_12/previous years 2018(final).pdf"
	
	elif year == 2019:
		key= "politicalsc/Previous_year_12/previous years 2019.pdf"
	
	elif year == 2020:
		key= "politicalsc/Previous_year_12/2020 board paper.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/PoliticalScience/Class12/Previous Yr')
def polprevXII():
	return render_template("prevyrclass12.html")

@app.route('/PoliticalScience/Class12/Important Questions')
def polimpXII():
	return render_template("polimp12.html")

@app.route('/PoliticalScience/Class12/Study notes')
def polnotesXII():
	return render_template("polnotesXII.html")
@app.route("/politicalsc/Class12/ncertquestions")
def polncertXII():
	return render_template("polncertXII.html")

@app.route("/politicalsc/Class12/ncertquestions/<string:questions>")	
def politicalncertXII(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "Chapter-1":
		key = "politicalsc/Pol12/BOOK1/ncert questions/ch-1 ncert.pdf"
	
	elif questions=="2":
		key = "politicalsc/Pol12/BOOK1/ncert questions/CHAPTER-3 ncert-converted.pdf"

	elif questions == "3":
		key = "politicalsc/Pol12/BOOK1/ncert questions/chapter-4 ncert-converted.pdf"
	
	elif questions == "4":
		key = "politicalsc/Pol12/BOOK1/ncert questions/chapter-5 NCERT.pdf"	
	
	elif questions=="5":
		key ="politicalsc/Pol12/BOOK1/ncert questions/chapter-6 ncert.pdf"

	elif questions=="6":
		key ="politicalsc/Pol12/BOOK1/ncert questions/chapter-7 ncert-converted.pdf"
	
	elif questions=="7":
		key ="politicalsc/Pol12/BOOK1/ncert questions/Chapter-8 ncert-converted.pdf"
	
	elif questions=="8":
		key ="politicalsc/Pol12/BOOK1/ncert questions/chapter-9 globalization ncert.pdf"
	
	elif questions=="9":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch1,2,3 book 2 ncert/book 2-chapter-1.pdf"
	
	elif questions=="10":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch1,2,3 book 2 ncert/book2 chapter-2.pdf"
	
	elif questions=="11":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch1,2,3 book 2 ncert/chapter-3.pdf"
		
	elif questions=="14":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch4,5,6 book 2 ncert/book2 chapter-6.pdf"
	
	elif questions=="12":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch4,5,6 book 2 ncert/book2 chapter3 and 4.pdf"
	
	elif questions=="13":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch4,5,6 book 2 ncert/book2 chapter 5.pdf"
	
	elif questions=="15":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch 7,8,9 book 2 ncert/book2 chapter-7.pdf"
	
	elif questions=="16":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch 7,8,9 book 2 ncert/book2 chapter-8.pdf"
	
	elif questions=="17":
		key ="politicalsc/Pol12/BOOK2/ncert questions/ch 7,8,9 book 2 ncert/book2 chapter-9.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route("/politicalsc/ncertquestions")
def polncert():
	return render_template("pol-ncert.html")
	
@app.route('/politicalsc/ncertquestions/<string:questions>/questions')
def PoliticalNcert(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "federalism":
		key = "politicalsc/NCERT class 10 POLITICAL SCIENCE/Federalism ncert.pdf"
	
	elif questions=="powersharing":
		key = "politicalsc/NCERT class 10 POLITICAL SCIENCE/class 10 civics chapter-1 NCERT.pdf"

	elif questions == "Democracy":
		key = "politicalsc/NCERT class 10 POLITICAL SCIENCE/DEMOCRACY AND DIVERSITY NCERT.pdf"
	
	elif questions == "outcomes":
		key = "politicalsc/NCERT class 10 POLITICAL SCIENCE/NCERT OUTCOMES OF DEMOCRACY.pdf"	
	
	elif questions=="political":
		key ="politicalsc/NCERT class 10 POLITICAL SCIENCE/ncert political parties.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)



@app.route('/PoliticalScience/Class12/<string:chapter_name>')
def politicalnotes12(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if chapter_name == "1":
		key = "politicalsc/Pol12/BOOK1/Notes/CHAPTER 1 NOTES.pdf"
	
	elif chapter_name=="2":
		key = "politicalsc/Pol12/BOOK1/Notes/chapter-2 notes.pdf"

	elif chapter_name == "3":
		key = "politicalsc/Pol12/BOOK1/Notes/CHAPTER-3 NOTES.pdf"
	
	elif chapter_name == "4":
		key = "politicalsc/Pol12/BOOK1/Notes/chapter-4 notes.pdf"	
	
	elif chapter_name=="5":
		key ="politicalsc/Pol12/BOOK1/Notes/chapter-5 notes final.pdf"

	elif chapter_name=="6":
		key ="politicalsc/Pol12/BOOK1/Notes/chapter-6 noters.pdf"

	elif chapter_name=="7":
		key ="politicalsc/Pol12/BOOK1/Notes/chapter-9 notes.pdf"

	elif chapter_name=="8":
		key ="politicalsc/Pol12/BOOK2/notes/book2-chapter 1.pdf"

	elif chapter_name=="9":
		key ="politicalsc/Pol12/BOOK2/notes/BOOK 2- CHAPTER 2 NOTES.pdf"
		
	elif chapter_name=="10":
		key ="politicalsc/Pol12/BOOK2/notes/book 2 chapter-3 notes final.pdf"
	
	elif chapter_name=="11":
		key ="politicalsc/Pol12/BOOK2/notes/book 2 chapter -4 notes.pdf"
	
	elif chapter_name=="12":
		key ="politicalsc/Pol12/BOOK2/notes/book 2 chapter-5 notes.pdf"
	
	elif chapter_name=="13":
		key ="politicalsc/Pol12/BOOK2/notes/chapter-6 book 2 notes.pdf"
	
	
	

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


##############################################################################################################################	

####################### class 10 English ##################################################################################



@app.route('/English/class 10/')
def English_Class_10():
	return render_template("English_class_10.html")



@app.route('/English/class 10/Previous Year')
def engprev():
	return render_template("EnglishPreviousYr_Class_10.html")

@app.route('/English/class 10/Important questions')
def engimp():
	return render_template("EnglishImpQue_Class_10.html")

@app.route('/English/class 10/Ncert Questions')
def engncert():
	return render_template('EnglishNcert_Class_10.html')

@app.route('/English/class 10/Study Notes')
def engnotes():
	return render_template('EnglishNotes_Class_10.html')





@app.route('/English/class 10/Important questions/<string:questions>')
def EnglishImpClass10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	
	if questions == "Anne":
		key = "English/class 10/Imp Questions/from the diary of Anne frank.pdf"
	
	elif questions=="glimpses":
		key = "English/class 10/Imp Questions/glimpses of india.pdf"

	elif questions == "hundred":
		key = "English/class 10/Imp Questions/hundred dresses 1.pdf"
	
	elif questions == "dresses":
		key = "English/class 10/Imp Questions/HUNDRED dresses 2.pdf"	
	
	elif questions=="god":
		key ="English/class 10/Imp Questions/Letter to god.pdf"
	
	elif questions=="Madam":
		key ="English/class 10/Imp Questions/Madam Rides the bus.pdf"
		
	elif questions=="Nelson":
		key ="English/class 10/Imp Questions/Nelson mandela.pdf"
		
	elif questions=="sermon":
		key ="English/class 10/Imp Questions/sermon at benaras.pdf"
		
	elif questions=="proposal":
		key ="English/class 10/Imp Questions/The proposal.pdf"
		
	elif questions=="bholi":
		key ="English/class 10/Imp Questions/Bholi.pdf"
		
	elif questions=="flying":
		key ="English/class 10/Imp Questions/two stories about flying.pdf"
	
	elif questions=="feet":
		key ="English/class 10/Imp Questions/Footprints without feet.pdf"
	
	elif questions=="hack":
		key ="English/class 10/Imp Questions/Hack driver.pdf"
	
	elif questions=="making":
		key ="English/class 10/Imp Questions/Making of a scientist.pdf"
	
	elif questions=="necklace":
		key ="English/class 10/Imp Questions/Necklace.pdf"
	
	elif questions=="story":
		key ="English/class 10/Imp Questions/Thiefs story.pdf"
	
	elif questions=="truimph":
		key ="English/class 10/Imp Questions/Triumph of Surgery.pdf"
	
	elif questions=="amanda":
		key ="English/class 10/Imp Questions/Amanda.pdf"
	
	elif questions=="animals":
		key ="English/class 10/Imp Questions/Animals.pdf"
	
	elif questions=="ball":
		key ="English/class 10/Imp Questions/Ball poem.pdf"
		
	elif questions=="dust":
		key ="English/class 10/Imp Questions/dust of snow.pdf"
	
	elif questions=="ice":
		key ="English/class 10/Imp Questions/Fire and Ice.pdf"
	
	elif questions=="custard":
		key ="English/class 10/Imp Questions/Tale of Custard the Dragon.pdf"
	
	elif questions=="zoo":
		key ="English/class 10/Imp Questions/Tiger in a zoo.pdf"

	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


@app.route('/English/class 10/Previous Year/<int:year>/')
def Englishpreviousyr(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "English/class 10/Previous Yr/2015.pdf"
	
	elif year == 2016:
		key= "English/class 10/Previous Yr/2016.pdf"
	
	elif year == 2017:
		key= "English/class 10/Previous Yr/2017.pdf"

	elif year == 2018:
		key= "English/class 10/Previous Yr/2018.pdf"
	
	elif year == 2019:
		key= "English/class 10/Previous Yr/2019.pdf"
	
	elif year == 2020:
		key= "English/class 10/Previous Yr/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/English/class 10/Study Notes/<string:chapter_name>')
def EnglishNotesClass10(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

		
	if questions == "Anne":
		key = "English/class 10/Notes/Diary of Anne FRank Notes.pdf"
	
	elif questions=="glimpses":
		key = "English/class 10/Notes/Glimpses of India NOTES.pdf"

	elif questions == "hundred":
		key = "English/class 10/Notes/Hundred Dresses 1 NOTES.pdf"
	
	elif questions == "dresses":
		key = "English/class 10/Notes/Hundred Dresses 2 NOTES.pdf"	
	
	elif questions=="god":
		key ="English/class 10/Notes/Letter to God Notes.pdf"
	
	elif questions=="Madam":
		key ="English/class 10/Notes/Madam rides the bus NOTES.pdf"
		
	elif questions=="Nelson":
		key ="English/class 10/Notes/Nelson MandelaNotes.pdf"
		
	elif questions=="sermon":
		key ="English/class 10/Notes/Serman at BenarasNOTES.pdf"
		
	elif questions=="proposal":
		key ="English/class 10/Notes/proposal NOTES.pdf"
		
	elif questions=="bholi":
		key ="English/class 10/Notes/Bholi Notes.pdf"
		
	elif questions=="flying":
		key ="English/class 10/Notes/two stories about flyingnotes.pdf"
	
	elif questions=="feet":
		key ="English/class 10/Notes/Foot prints wihout feetNotes.pdf"
	
	elif questions=="hack":
		key ="English/class 10/Notes/hack driver Notes.pdf"
	
	elif questions=="making":
		key ="English/class 10/Notes/Making of a ScientistNotes.pdf"
	
	elif questions=="necklace":
		key ="English/class 10/Notes/Necklace Notes.pdf"
	
	elif questions=="story":
		key ="English/class 10/Notes/a thief's story Notes.pdf"
	
	elif questions=="truimph":
		key ="English/class 10/Notes/A triumph notes.pdf"
	
	elif questions=="amanda":
		key ="English/class 10/Notes/Amanda Notes.pdf"
	
	elif questions=="animals":
		key ="English/class 10/Notes/animals notes.pdf"
	
	elif questions=="ball":
		key ="English/class 10/Notes/Ball poemNotes.pdf"
		
	elif questions=="dust":
		key ="English/class 10/Notes/dust of snowNotes.pdf"
	
	elif questions=="ice":
		key ="English/class 10/Notes/fire and iceNotes.pdf"
	
	elif questions=="custard":
		key ="English/class 10/Notes/a tale Notes.pdf"
	
	elif questions=="zoo":
		key ="English/class 10/Notes/tiger in a zooNotes.pdf"
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/English/class 10/Ncert Questions/<string:questions>')
def EnglishNcert_Class10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
			
	if questions == "Anne":
		key = "English/class 10/Ncert Solutions/Dairy of Anne Frank Ncert.pdf"
	
	elif questions=="glimpses":
		key = "English/class 10/Ncert Solutions/Glimpses of India NCERT.pdf"

	elif questions == "hundred":
		key = "English/class 10/Ncert Solutions/Hundred Dresses 1 NCERT FOLDER.pdf"
	
	elif questions == "dresses":
		key = "English/class 10/Ncert Solutions/Hundred Dresses 2 NCERT FOLDER.pdf"	
	
	elif questions=="god":
		key ="English/class 10/Ncert Solutions/letter to God NCERT.pdf"
	
	elif questions=="Madam":
		key ="English/class 10/Ncert Solutions/Madam rides the bus NCERT FOLDER.pdf"
		
	elif questions=="Nelson":
		key ="English/class 10/Ncert Solutions/Melson MadelaNCERT solutiosn.pdf"
		
	elif questions=="sermon":
		key ="English/class 10/Ncert Solutions/Sermon at BenarasNCERT FOLDER.pdf"
		
	elif questions=="proposal":
		key ="English/class 10/Ncert Solutions/Proposal NCERT FOLDER.pdf"
		
	elif questions=="bholi":
		key ="English/class 10/Ncert Solutions/Bholi NCERT solutions.pdf"
		
	elif questions=="flying":
		key ="English/class 10/Ncert Solutions/two stories about flyingNCERT FOLDER.pdf"
	
	elif questions=="feet":
		key ="English/class 10/Ncert Solutions/Footprints wihtout feetNCERT Solutions.pdf"
	
	elif questions=="hack":
		key ="English/class 10/Ncert Solutions/Hack driverNCERT solutions.pdf"
	
	elif questions=="making":
		key ="English/class 10/Ncert Solutions/Making of s scientist NCERT SOLUTIONS.pdf"
	
	elif questions=="necklace":
		key ="English/class 10/Ncert Solutions/Necklace NCERT SOLUTIONS.pdf"
	
	elif questions=="story":
		key ="English/class 10/Ncert Solutions/atheifs story NCERT Solutions.pdf"
	
	elif questions=="truimph":
		key ="English/class 10/Ncert Solutions/a atriumph NCERT solutions.pdf"
	
	elif questions=="amanda":
		key ="English/class 10/Ncert Solutions/Amanda NCERT solutions.pdf"
	
	elif questions=="animals":
		key ="English/class 10/Ncert Solutions/Animals NCERT solutiosn.pdf"
	
	elif questions=="ball":
		key ="English/class 10/Ncert Solutions/Ball poemNCERT solutions.pdf"
		
	elif questions=="dust":
		key ="English/class 10/Ncert Solutions/dust of snowNCERT solutions.pdf"
	
	elif questions=="ice":
		key ="English/class 10/Ncert Solutions/Fire and iceNCERT solutions.pdf"
	
	elif questions=="custard":
		key ="English/class 10/Ncert Solutions/a taleNCERT solutions.pdf"
	
	elif questions=="zoo":
		key ="English/class 10/Ncert Solutions/Tiger in a zooNCERT Solutions.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

######################################## Class 12 English #############################################################################

@app.route('/English/Class 12/')
def English_Class_12():
	return render_template("English_class_12.html")



@app.route('/English/Class 12/Previous Year')
def engprev12():
	return render_template("EnglishPreviousYr_Class_12.html")

@app.route('/English/Class 12/Important questions')
def engimp12():
	return render_template("EnglishImpQue_Class_12.html")

@app.route('/English/Class 12/Ncert Questions')
def engncert12():
	return render_template('EnglishNcert_Class_12.html')

@app.route('/English/Class 12/Study Notes')
def engnotes12():
	return render_template('EnglishNotes_Class_12.html')


@app.route('/English/Class 12/Important questions/<string:questions>')
def EnglishImpClass12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "slum":
		key = "English/class 12/Imp Questions/An elementray school classroom in a slum Important questions.pdf"
	
	elif questions=="thing":
		key = "English/class 12/Imp Questions/A Thing of Beauty Important questions.pdf"

	elif questions == "aunt":
		key = "English/class 12/Imp Questions/Aunt jennifers tigers Important Questions.pdf"
	
	elif questions == "deep":
		key = "English/class 12/Imp Questions/Deep water Important questions.pdf"	
	
	elif questions=="evans":
		key ="English/class 12/Imp Questions/Evans tries an O-level  Important Questions.pdf"
	
	elif questions=="indigo":
		key ="English/class 12/Imp Questions/Indigo Important questions.pdf"
		
	elif questions=="quiet":
		key ="English/class 12/Imp Questions/keeping quietImportant questions.pdf"
		
	elif questions=="lost":
		key ="English/class 12/Imp Questions/Lost spring Important questions.pdf"
		
	elif questions=="sixty":
		key ="English/class 12/Imp Questions/My Mother at Sixty Six Important questions.pdf"
		
	elif questions=="face":
		key ="English/class 12/Imp Questions/On the face of it Important questions.pdf"
		
	elif questions=="wizard":
		key ="English/class 12/Imp Questions/Should wizrad hit mommy Important Questions.pdf"
	
	elif questions=="enemy":
		key ="English/class 12/Imp Questions/The Enemy Important questions.pdf"
	
	elif questions=="last":
		key ="English/class 12/Imp Questions/The last lesson Important questions.pdf"
	
	elif questions=="rattrap":
		key ="English/class 12/Imp Questions/The Rattrap Important questions.pdf"
	
	elif questions=="Third":
		key ="English/class 12/Imp Questions/The Third level Important questions.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


@app.route('/English/Class 12/Previous Year/<int:year>/')
def EnglishpreviousyrClass12(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "English/class 12/Previous Yr/2015.pdf"
	
	elif year == 2016:
		key= "English/class 12/Previous Yr/2016.pdf"
	
	elif year == 2017:
		key= "English/class 12/Previous Yr/2017.pdf"

	elif year == 2018:
		key= "English/class 12/Previous Yr/2018.pdf"
	
	elif year == 2019:
		key= "English/class 12/Previous Yr/2019.pdf"
	
	elif year == 2020:
		key= "English/class 12/Previous Yr/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/English/Class 12/Study Notes/<string:chapter_name>')
def EnglishNotesClass12(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if questions == "slum":
		key = "English/class 12/Notes/An elementray school classroom in a slum notes.pdf"
	
	elif questions=="thing":
		key = "English/class 12/Notes/A Thing of Beauty Notes.pdf"

	elif questions == "aunt":
		key = "English/class 12/Notes/Aunt jennifers tigers Notes.pdf"
	
	elif questions == "deep":
		key = "English/class 12/Notes/Deep water notes.pdf"	
	
	elif questions=="evans":
		key ="English/class 12/Notes/Evans tries an O-level notes.pdf"
	
	elif questions=="indigo":
		key ="English/class 12/Notes/Indigo Notes.pdf"
		
	elif questions=="quiet":
		key ="English/class 12/Notes/Keeping Quiet notes.pdf"
		
	elif questions=="lost":
		key ="English/class 12/Notes/Lost spring notes.pdf"
		
	elif questions=="sixty":
		key ="English/class 12/Notes/My Mother at Sixty Six notes.pdf"
		
	elif questions=="face":
		key ="English/class 12/Notes/On the face of it notes.pdf"
		
	elif questions=="wizard":
		key ="English/class 12/Notes/Should wizrad hit mommy notes.pdf"
	
	elif questions=="enemy":
		key ="English/class 12/Notes/The Enemy Notes.pdf"
	
	elif questions=="last":
		key ="English/class 12/Notes/The Last Lesson notes.pdf"
	
	elif questions=="rattrap":
		key ="English/class 12/Notes/The Rattrap Notes.pdf"
	
	elif questions=="Third":
		key ="English/class 12/Notes/The Third level Notes.pdf"

	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/English/Class 12/Ncert Questions/<string:questions>')
def EnglishNcert_Class12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "slum":
		key = "English/class 12/Ncert Questions/An elementray school classroom in a slum NCERT solutions.pdf"
	
	elif questions=="thing":
		key = "English/class 12/Ncert Questions/A Thing of Beauty NCERT solutions.pdf"

	elif questions == "aunt":
		key = "English/class 12/Ncert Questions/Aunt jennifers tigers NCERT solutions.pdf"
	
	elif questions == "deep":
		key = "English/class 12/Ncert Questions/Deep water NCERT solutions.pdf"	
	
	elif questions=="evans":
		key ="English/class 12/Ncert Questions/Evans tries an O-level  NCERT solutions.pdf"
	
	elif questions=="indigo":
		key ="English/class 12/Ncert Questions/Indigo NCERT solutions.pdf"
		
	elif questions=="quiet":
		key ="English/class 12/Ncert Questions/Keeping quiet NCERT solutions.pdf"
		
	elif questions=="lost":
		key ="English/class 12/Ncert Questions/Lost spring NCERT solutions.pdf"
		
	elif questions=="sixty":
		key ="English/class 12/Imp Questions/My Mother at Sixty Six NCERT Solutions.pdf"
		
	elif questions=="face":
		key ="English/class 12/Ncert Questions/On the face of it NCERT solutions.pdf"
		
	elif questions=="wizard":
		key ="English/class 12/Ncert Questions/Should wizrad hit mommy NCERT solutions.pdf"
	
	elif questions=="enemy":
		key ="English/class 12/Ncert Questions/The Enemy NCERT Solutions.pdf"
	
	elif questions=="last":
		key ="English/class 12/Ncert Questions/The last lesson ncert solutions.pdf"
	
	elif questions=="rattrap":
		key ="English/class 12/Ncert Questions/The Rattrap NCERT folder.pdf"
	
	elif questions=="Third":
		key ="English/class 12/Ncert Questions/The Third level NCERT Solutions.pdf"

	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)



################################################################################################################################
# Economics class 10
@app.route('/Economics/class 10/')
def Economics_Class_10():
	return render_template("Economics_class_10.html")



@app.route('/Economics/class 10/Previous Year')
def ecoprev():
	return render_template("EconomicsPreviousYr_Class_10.html")

@app.route('/Economics/class 10/Important questions')
def ecoimp():
	return render_template("EconomicsImpQue_Class_10.html")

@app.route('/Economics/class 10/Ncert Questions')
def econcert():
	return render_template('EconomicsNcert_Class_10.html')

@app.route('/Economics/class 10/Study Notes')
def econotes():
	return render_template('EconomicsNotes_Class_10.html')



@app.route('/Economics/class 10/Study Notes/<string:chapter_name>')
def EconomicsNotesClass10(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if chapter_name == "consumer":
		key = "Economics/class 10/Notes/CONSUMER RIGHTS CH-5 NOTES.pdf"
	
	elif chapter_name=="development":
		key = "Economics/class 10/Notes/DEVELOPMENT CH-1 NOTES.pdf"

	elif chapter_name == "global":
		key = "Economics/class 10/Notes/GLOBALIZATION AND INDIAN ECONOMY CH-4 NOTES.pdf"
	
	elif chapter_name == "money":
		key = "Economics/class 10/Notes/MONEY AND CREDIT CH-3 NOTES.pdf"	
	
	elif chapter_name=="sectors":
		key ="Economics/class 10/Notes/SECTORS OF INDIAN ECONOMY CH-2 NOTES.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/Economics/class 10/Ncert Questions/<string:questions>')
def EconomicsNcert_Class10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "consumer":
		key = "Economics/class 10/Ncert Solution/CONSUMER RIGHTS CH-5 NCERT.pdf"
	
	elif questions=="development":
		key = "Economics/class 10/Ncert Solution/DEVELOPMENT CH-1 NCERT.pdf"

	elif questions == "global":
		key = "Economics/class 10/Ncert Solution/GLOBALIZATION AND INDIAN ECONOMY CH-4 NCERT.pdf"
	
	elif questions == "money":
		key = "Economics/class 10/Ncert Solution/MONEY AND CREDIT CH-3 NCERT.pdf"	
	
	elif questions=="sectors":
		key ="Economics/class 10/Ncert Solution/SECTORS OF INDIAN ECONOMY CH-2 NCERT.pdf"
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)






# Economics Class 12##############################################################################################################
@app.route('/Economics/Class 12/')
def Economics_Class_12():
	return render_template("Economics_class_12.html")

@app.route('/Economics/Class 12/Previous Year')
def ecoprev12():
	return render_template("EconomicsPreviousYr_Class_12.html")

@app.route('/Economics/Class 12/Important questions')
def ecoimp12():
	return render_template("EconomicsImpQue_Class_12.html")

@app.route('/Economics/Class 12/Ncert Questions')
def econcert12():
	return render_template('EconomicsNcert_Class_12.html')

@app.route('/Economics/Class 12/Study Notes')
def econotes12():
	return render_template('EconomicsNotes_Class_12.html')


# Economics Class 12 document modules #####################################

@app.route('/Economics/Class 12/Important questions/<string:questions>')
def EconomicsImpClass12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "Income":
		key = "Economics/Class 12/Imp Questions/Determination of Income and Employment  CH-4 Imp Questions.pdf"
	
	elif questions=="govt":
		key = "Economics/Class 12/Imp Questions/Government Budget and the Economy Ch-5 Imp Questions.pdf"

	elif questions == "macro":
		key = "Economics/Class 12/Imp Questions/Introductory Macroeconomics  Ch-1 IMp Questions.pdf"
	
	elif questions == "money":
		key = "Economics/Class 12/Imp Questions/Money and Banking  Ch-3 Imp Questions.pdf"	
	
	elif questions=="national":
		key ="Economics/Class 12/Imp Questions/National Income and Related Aggregates Ch-2 imp questions.pdf"

	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


@app.route('/Economics/Class 12/Previous Year/<int:year>/')
def EconomicspreviousyrClass12(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "Economics/Class 12/Previous Yr/2015.pdf"
	
	elif year == 2016:
		key= "Economics/Class 12/Previous Yr/2016.pdf"
	
	elif year == 2017:
		key= "Economics/Class 12/Previous Yr/2017.pdf"

	elif year == 2018:
		key= "Economics/Class 12/Previous Yr/2018.pdf"
	
	elif year == 2019:
		key= "Economics/Class 12/Previous Yr/2019.pdf"
	
	elif year == 2020:
		key= "Economics/Class 12/Previous Yr/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/Economics/Class 12/Study Notes/<string:chapter_name>')
def EconomicsNotesClass12(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if chapter_name == "Ch-1":
		key = "Economics/Class 12/Notes/Ch-1.pdf"
	
	elif chapter_name=="Ch-2":
		key = "Economics/Class 12/Notes/Ch-2.pdf"

	elif chapter_name == "Ch-3":
		key = "Economics/Class 12/Notes/Ch-3.pdf"
	
	elif chapter_name == "Ch-4":
		key = "Economics/Class 12/Notes/Ch-4.pdf"	
	
	elif chapter_name=="Ch-5":
		key ="Economics/Class 12/Notes/Ch-5.pdf"
	
	elif chapter_name=="Ch-6":
		key ="Economics/Class 12/Notes/Ch-6.pdf"

	elif chapter_name=="Comparative":
		key ="Economics/Class 12/Notes/COMPARATIVE DEVELOPMENT EXPERIENCE OF INDIA AND ITS CH-10 notes.pdf"
	
	elif chapter_name=="growth":
		key ="Economics/Class 12/Notes/EMPLOYMENT GROWTH AND OTHER ISSUES. CH-7 notes.pdf"
		
	elif chapter_name=="sustainable":
		key ="Economics/Class 12/Notes/ENVIRONMENT AND SUSTAINABLE DEVELOPMENT CH-9 notes.pdf"
		
	elif chapter_name=="capital":
		key ="Economics/Class 12/Notes/HUMAN CAPITAL FORMATION IN INDIA CH-5 notes.pdf"
		
	elif chapter_name=="economy":
		key ="Economics/Class 12/Notes/INDIAN ECONOMY 1950-1990 CH-2 NOTES.pdf"
		
	elif chapter_name=="eve":
		key ="Economics/Class 12/Notes/INDIAN ECONOMY ON THE EVE OF INDEPENDENCE CH-1 NOTES.pdf"
		
	elif chapter_name=="infrastructure":
		key ="Economics/Class 12/Notes/INFRASTRUCTURE CH-8 notes.pdf"
		
	elif chapter_name=="liberal":
		key ="Economics/Class 12/Notes/LIBERALIZATION, PRIVATIZATION AND GLOBALIZATION CH-3notes.pdf"
		
	elif chapter_name=="poverty":
		key ="Economics/Class 12/Notes/POVERTY CH-4 notes.pdf"
		
	elif chapter_name=="rural":
		key ="Economics/Class 12/Notes/RURAL DEVELOPMENT CH-6 notes.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/Economics/Class 12/Ncert Questions/<string:questions>')
def EconomicsNcert_Class12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "balance":
		key = "Economics/Class 12/Ncert Questions/Balance of Payments Ch-6 NCERT.pdf"
	
	elif questions=="comparative":
		key = "Economics/Class 12/Ncert Questions/COMPARATIVE DEVELOPMENT EXPERIENCE OF INDIA AND ITS CH-10 NCERT.pdf"

	elif questions == "determination":
		key = "Economics/Class 12/Ncert Questions/Determination of Income and Employment  Ch-4 NCERT.pdf"
	
	elif questions == "Employment":
		key = "Economics/Class 12/Ncert Questions/EMPLOYMENT GROWTH AND OTHER ISSUES. CH-7 NCERT.pdf"	
	
	elif questions=="Budget":
		key ="Economics/Class 12/Ncert Questions/Government Budget and the Economy Ch-5 NCERT.pdf"

	elif questions=="capital":
		key ="Economics/Class 12/Ncert Questions/HUMAN CAPITAL FORMATION IN INDIA CH-5 NCERT.pdf"
		
	elif questions=="economy":
		key ="Economics/Class 12/Ncert Questions/INDIAN ECONOMY 1950-1990 CH-2 NCERT.pdf"
		
	elif questions=="independence":
		key ="Economics/Class 12/Ncert Questions/INDIAN ECONOMY ON THE EVE OF INDEPENDENCE CH-1 NCERT.pdf"
		
	elif questions=="macroeconomics":
		key ="Economics/Class 12/Ncert Questions/Introductory Macroeconomics  Ch-1.pdf"
		
	elif questions=="privatization":
		key ="Economics/Class 12/Ncert Questions/LIBERALIZATION, PRIVATIZATION AND GLOBALIZATION CH-3 NCERT.pdf"
		
	elif questions=="money":
		key ="Economics/Class 12/Ncert Questions/Money and Banking  Ch-3 Ncert.pdf"
		
	elif questions=="aggregates":
		key ="Economics/Class 12/Ncert Questions/National Income and Related Aggregates Ch-2 Ncert.pdf"
		
	elif questions=="poverty":
		key ="Economics/Class 12/Ncert Questions/POVERTY CH-4 NCERT.pdf"
		
	elif questions=="rural":
		key ="Economics/Class 12/Ncert Questions/RURAL DEVELOPMENT CH-6 NCERT.pdf"
		
				
	elif questions=="Sustainability":
		key ="Economics/Class 12/Ncert Questions/ENVIRONMENT AND SUSTAINABLE DEVELOPMENT CH-9 NCERT.pdf"	
	
	elif questions=="Infrastructure":
		key ="Economics/Class 12/Ncert Questions/INFRASTRUCTURE CH-8 NCERT.pdf"
							
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
#######################################################################################################################################

##############################################################################################################################
# Geography class 10
@app.route('/Geography/class 10/')
def Geography_Class_10():
	return render_template("Geography_class_10.html")


@app.route('/Geography/class 10/Important questions')
def geoimp():
	return render_template("GeographyImpQue_Class_10.html")

@app.route('/Geography/class 10/Ncert Questions')
def geoncert():
	return render_template('GeographyNcert_Class_10.html')

@app.route('/Geography/class 10/Study Notes')
def geonotes():
	return render_template('GeographyNotes_Class_10.html')

# Geography class 10 document modules
@app.route('/Geography/class 10/Important questions/<string:questions>')
def GeographyImpClass10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "agriculture":
		key = "Geography/class 10/Important Questions/Agriculture ch-4 important questions.pdf"
	
	elif questions=="lifeline":
		key = "Geography/class 10/Important Questions/Lifeline of National Economy  ch-7 important questions.pdf"

	elif questions == "manufacturing":
		key = "Geography/class 10/Important Questions/Manufacturing Industries chapter-6 important questions.pdf"
	
	elif questions == "minerals":
		key = "Geography/class 10/Important Questions/Minerals and Energy Resources chapter-5 important questions.pdf"	
	
	elif questions=="resources":
		key ="Geography/class 10/Important Questions/Resources and Development ch-1 important questions.pdf"

	elif questions=="water":
		key ="Geography/class 10/Important Questions/Water Resources chapter-3 important questions.pdf"
	
		
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)



@app.route('/Geography/class 10/Study Notes/<string:chapter_name>')
def GeographyNotesClass10(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if chapter_name == "Agriculture":
		key = "Geography/class 10/Notes/agriculture notes.pdf"
	
	elif chapter_name=="lifeline":
		key = "Geography/class 10/Notes/Lifelines of National Economy ch-7 geography notes.pdf"

	elif chapter_name == "manufacturing":
		key = "Geography/class 10/Notes/manufacturing industries notes.pdf"
	
	elif chapter_name == "minerals":
		key = "Geography/class 10/Notes/minerals notes.pdf"	
	
	elif chapter_name=="resource":
		key ="Geography/class 10/Notes/resource and development notes.pdf"
	
	elif chapter_name=="water":
		key ="Geography/class 10/Notes/water notes.pdf"

	

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/Geography/class 10/Ncert Questions/<string:questions>/questions')
def GeographyNcert_Class10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "Agriculture":
		key = "Geography/class 10/Ncert Solutions/Agriculture ch-4 Geography ncert.pdf"
	
	elif questions=="lifeline":
		key = "Geography/class 10/Ncert Solutions/Lifelines of National Economy chapter-7 ncert geography.pdf"

	elif questions == "manufacturing":
		key = "Geography/class 10/Ncert Solutions/Manufacturing Industries CHAPTER-6 NCERT GEOGRAPHY.pdf"
	
	elif questions == "minerals":
		key = "Geography/class 10/Ncert Solutions/Minerals and Energy Resources ch-5 Geography ncert.pdf"	
	
	elif questions=="resource":
		key ="Geography/class 10/Ncert Solutions/Resource and Development CH-1 GEOGRAPHY NCERT.pdf"
	
	elif questions=="water":
		key ="Geography/class 10/Ncert Solutions/Water resource CHAPTER-3 NCERT GEOGRAPHY.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)



######################################################################################################################################


# Geography Class 12
@app.route('/Geography/Class 12/')
def Geography_Class_12():
	return render_template("Geography_class_12.html")

@app.route('/Geography/Class 12/Previous Year')
def geoprev12():
	return render_template("GeographyPreviousYr_Class_12.html")

@app.route('/Geography/Class 12/Important questions')
def geoimp12():
	return render_template("GeographyImpQue_Class_12.html")

@app.route('/Geography/Class 12/Ncert Questions')
def geoncert12():
	return render_template('GeographyNcert_Class_12.html')

@app.route('/Geography/Class 12/Study Notes')
def geonotes12():
	return render_template('GeographyNotes_Class_12.html')


# Geography Class 12 document modules

@app.route('/Geography/Class 12/Important questions/<string:questions>')
def GeographyImpClass12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "geographical":
		key = "Geography/Class 12/Imp Questions/PART B GEOGRAPHICAL PERSPECTIVE.pdf"
	
	elif questions=="human":
		key = "Geography/Class 12/Imp Questions/PART B HUMAN DEVELOPMENT.pdf"

	elif questions == "settlements":
		key = "Geography/Class 12/Imp Questions/PART B HUMAN SETTLEMENTS.pdf"
	
	elif questions == "migration":
		key = "Geography/Class 12/Imp Questions/PART B MIGRATION.pdf"	
	
	elif questions=="energy":
		key ="Geography/Class 12/Imp Questions/PART B MINERAL AND ENERGY RESOURCES.pdf"
		
	elif questions=="planning":
		key ="Geography/Class 12/Imp Questions/PART B PLANNING AND SUSTAINABLE DEVELOPMENT.pdf"
		
		
	elif questions=="water":
		key ="Geography/Class 12/Imp Questions/PART B WATER RESOURCES.pdf"
		
	elif questions=="human-geo":
		key ="Geography/Class 12/Imp Questions/human geography-important questions.pdf"
		
	elif questions=="human-develop":
		key ="Geography/Class 12/Imp Questions/PART A HUMAN DEVELOPMENT.pdf"
		
	elif questions=="population":
		key ="Geography/Class 12/Imp Questions/PART B POPULATION.pdf"
	
	elif questions=="human-settle":
		key ="Geography/Class 12/Imp Questions/PART A HUMAN SETTLEMENT.pdf"
		
	elif questions=="activities":
		key ="Geography/Class 12/Imp Questions/PART A PRIMARY ACTIVITIES.pdf"
		
	elif questions=="tertiary":
		key ="Geography/Class 12/Imp Questions/PART A TERTIARY ACTIVITIES.pdf"
		
	elif questions=="world":
		key ="Geography/Class 12/Imp Questions/world population-important questions.pdf"
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


@app.route('/Geography/Class 12/Previous Year/<int:year>/')
def GeographypreviousyrClass12(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "Geography/Class 12/Previous Yr/2015.pdf"
	
	elif year == 2016:
		key= "Geography/Class 12/Previous Yr/2016.pdf"
	
	elif year == 2017:
		key= "Geography/Class 12/Previous Yr/2017.pdf"

	elif year == 2018:
		key= "Geography/Class 12/Previous Yr/2018.pdf"
	
	elif year == 2019:
		key= "Geography/Class 12/Previous Yr/2019.pdf"
	
	elif year == 2020:
		key= "Geography/Class 12/Previous Yr/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/Geography/Class 12/Study Notes/<string:questions>')
def GeographyNotesClass12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if questions == "human":
		key = "Geography/Class 12/Notes/HUMAN DEVELOPMENT.pdf"
	
	elif questions=="nature":
		key = "Geography/Class 12/Notes/human geography.pdf"

	elif questions == "settlements":
		key = "Geography/Class 12/Notes/HUMAN SETTLEMENTS.pdf"
	
	elif questions == "population":
		key = "Geography/Class 12/Notes/POPULATION COMPOSITION.pdf"	
	
	elif questions=="primary":
		key ="Geography/Class 12/Notes/PRIMARY ACTIVITTIES.pdf"

	elif questions=="tertiary":
		key ="Geography/Class 12/Notes/TERTIARY ACTIVITIES.pdf"

	elif questions=="world":
		key ="Geography/Class 12/Notes/WORLD POPULATION.pdf"

	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/Geography/Class 12/Ncert Questions/<string:questions>')
def GeographyNcert_Class12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "human":
		key = "Geography/Class 12/Ncert solutions/HUMAN DEVELOPMENT NCERT.pdf"
	
	elif questions=="nature":
		key = "Geography/Class 12/Ncert solutions/human geography nature and scope- ncert.pdf"

	elif questions == "settlements":
		key = "Geography/Class 12/Ncert solutions/HUMAN SETTLEMENTS NCERT.pdf"
	
	elif questions == "population":
		key = "Geography/Class 12/Ncert solutions/population composition ncert.pdf"	
	
	elif questions=="primary":
		key ="Geography/Class 12/Ncert solutions/PRIMARY ACTIVITIES NCERT.pdf"

	elif questions=="tertiary":
		key ="Geography/Class 12/Ncert solutions/tertiary activities ncert.pdf"

	elif questions=="world":
		key ="Geography/Class 12/Ncert solutions/world population-ncert.pdf"
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
########################################################################################################################################

####################################################################################################################################
# History class 10
@app.route('/History/class 10/')
def History_Class_10():
	return render_template("History_class_10.html")



@app.route('/History/class 10/Previous Year')
def hisprev():
	return render_template("HistoryPreviousYr_Class_10.html")

@app.route('/History/class 10/Important questions')
def hisimp():
	return render_template("HistoryImpQue_Class_10.html")

@app.route('/History/class 10/Ncert Questions')
def hisncert():
	return render_template('HistoryNcert_Class_10.html')

@app.route('/History/class 10/Study Notes')
def hisnotes():
	return render_template('HistoryNotes_Class_10.html')

# History class 10 document modules
@app.route('/History/class 10/Important questions/<string:questions>')
def HistoryImpClass10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "rise":
		key = "History/Class 10/Imp Questions/Part A Ch-1THE RISE OF NATIONALISM IN EUROPE Imp Questions.pdf"
	
	elif questions=="nationalism":
		key = "History/Class 10/Imp Questions/Part A Ch-2 Nationalism In India Imp Questions.pdf"

	elif questions == "age":
		key = "History/Class 10/Imp Questions/Part B Ch-2 THE AGE OF INDUSTRIALIZATIONImp Questions.pdf"
	
	elif questions == "global":
		key = "History/Class 10/Imp Questions/Part B ch-1THE MAKING OF A GLOBAL WORLD Imp Questions.pdf"	
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)




@app.route('/History/class 10/Study Notes/<string:questions>')
def HistoryNotesClass10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if questions == "rise":
		key = "History/Class 10/Notes/Part A Ch-1THE RISE OF NATIONALISM IN EUROPE NOtes.pdf"
	
	elif questions=="nationalism":
		key = "History/Class 10/Notes/Part A Ch-2 Nationalism in IndiaNotes.pdf"

	elif questions == "age":
		key = "History/Class 10/Notes/Part B Ch-2 THE AGE OF INDUSTRIALIZATIONNotes.pdf"
	
	elif questions == "global":
		key = "History/Class 10/Notes/Part B ch-1THE MAKING OF A GLOBAL WORLD Notes.pdf"	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
	

@app.route('/History/class 10/Ncert Questions/<string:questions>')
def HistoryNcert_Class10(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "rise":
		key = "History/Class 10/Ncert Questions/Part A Ch-1 THE RISE OF NATIONALISM IN EUROPENcert.pdf"
	
	elif questions=="nationalism":
		key = "History/Class 10/Ncert Questions/Part A Ch-2 Nationalims in India Ncert.pdf"

	elif questions == "age":
		key = "History/Class 10/Ncert Questions/Part B ch-2 THE AGE OF INDUSTRIALIZATIONNCERT.pdf"
	
	elif questions == "global":
		key = "History/Class 10/Ncert Questions/Part B ch-1 THE MAKING OF A GLOBAL WORLDNCERT.pdf"	
	
		
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


# History Class 12 #################################################################################################################
@app.route('/History/Class 12/')
def History_Class_12():
	return render_template("History_class_12.html")

@app.route('/History/Class 12/Previous Year')
def hisprev12():
	return render_template("HistoryPreviousYr_Class_12.html")

@app.route('/History/Class 12/Important questions')
def hisimp12():
	return render_template("HistoryImpQue_Class_12.html")

@app.route('/History/Class 12/Ncert Questions')
def hisncert12():
	return render_template('HistoryNcert_Class_12.html')

@app.route('/History/Class 12/Study Notes')
def hisnotes12():
	return render_template('HistoryNotes_Class_12.html')


# History Class 12 document modules

@app.route('/History/Class 12/Important questions/<string:questions>')
def HistoryImpClass12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "imperial":
		key = "History/Class 12/Imp Questions/an imperial capital vijayanagar-important.pdf"
	
	elif questions=="sufi":
		key = "History/Class 12/Imp Questions/Bhakti-sufi traditions-imp.pdf"

	elif questions == "beads":
		key = "History/Class 12/Imp Questions/Bricks, Beads and Bones The Harappan Civilisation Ncert.pdf"
	
	elif questions == "kings":
		key = "History/Class 12/Imp Questions/kings and chronicles-important.pdf"	
	
	elif questions=="caste":
		key ="History/Class 12/Imp Questions/Kinship,caste and class imp.pdf"
		
	elif questions=="peasants":
		key ="History/Class 12/Imp Questions/peasants,zamindars and state-important.pdf"
		
	elif questions=="Thinkers":
		key ="History/Class 12/Imp Questions/Thinkers,belief,buildingsculture development-imp.pdf"
	
	elif questions=="eyes":
		key ="History/Class 12/Imp Questions/Through the eyes of travellers-imp.pdf"
	
	elif questions=="farmers":
		key ="History/Class 12/Imp Questions/Kings,farmers and towns-imp.pdf"
	
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)


@app.route('/History/Class 12/Previous Year/<int:year>/')
def HistorypreviousyrClass12(year):
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	
	if year == 2015:
		key = "History/Class 12/Previous yr/2015.pdf"
	
	elif year == 2016:
		key= "History/Class 12/Previous yr/2016.pdf"
	
	elif year == 2017:
		key= "History/Class 12/Previous yr/2017.pdf"

	elif year == 2018:
		key= "History/Class 12/Previous yr/2018.pdf"
	
	elif year == 2019:
		key= "History/Class 12/Previous yr/2019.pdf"
	
	elif year == 2020:
		key= "History/Class 12/Previous yr/2020.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

@app.route('/History/Class 12/Study Notes/<string:chapter_name>')
def HistoryNotesClass12(chapter_name):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)

	if chapter_name == "imperial":
		key = "History/Class 12/Notes/An imperial capital-notes.pdf"
	
	elif chapter_name=="sufi":
		key = "History/Class 12/Notes/Bhakti-sufi traditions-notes.pdf"

	elif chapter_name == "beads":
		key = "History/Class 12/Notes/Bricks, beads and bones-notes.pdf"
	
	elif chapter_name == "Colonialism":
		key = "History/Class 12/Notes/Colonialism and the countryside-notes.pdf"	
	
	elif chapter_name=="Framing":
		key ="History/Class 12/Notes/Framing the constitution-notes.pdf"
	
	elif chapter_name=="Kings":
		key ="History/Class 12/Notes/Kings and the chronicals-notes.pdf"
	
	elif chapter_name=="farmers":
		key ="History/Class 12/Notes/Kings, farmers and towns-notes.pdf"
			
	elif chapter_name=="caste":
		key ="History/Class 12/Notes/Kinship,caste and class notes.pdf"
		
	elif chapter_name=="gandhi":
		key ="History/Class 12/Notes/Mahatama gandhi and nationalist movement-notes"
		
	elif chapter_name=="Rebels":
		key ="History/Class 12/Notes/Rebels and Raj-notes.pdf"
		
	elif chapter_name=="Thinkers":
		key ="History/Class 12/Notes/Thinkers, beliefs and buildingd-notes.pdf"
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
    	

@app.route('/History/Class 12/Ncert Questions/<string:questions>')
def HistoryNcert_Class12(questions):
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(BUCKET_NAME)
	
	if questions == "imperial":
		key = "History/Class 12/Ncert Questions/An imperial capital Vijaynagara-ncert.pdf"
	
	elif questions=="sufi":
		key = "History/Class 12/Ncert Questions/Bhakti-sufi traditions ncert.pdf"

	elif questions == "beads":
		key = "History/Class 12/Ncert Questions/Bricks, Beads and Bones The Harappan Civilisation Ncert.pdf"
	
	elif questions == "colonial":
		key = "History/Class 12/Ncert Questions/colonial cities ncert.pdf"	
	
	elif questions=="colonialism":
		key ="History/Class 12/Ncert Questions/Colonialism and the countryside-ncert.pdf"
	
	elif questions=="framing":
		key = "History/Class 12/Ncert Questions/FRAMING THE CONSTITUTION.pdf"

	elif questions == "kings":
		key = "History/Class 12/Ncert Questions/Kings and chronicals the mughal courts-ncert.pdf"
	
	elif questions == "farmers":
		key = "History/Class 12/Ncert Questions/Kings, farmers and towns ncert.pdf"	
	
	elif questions=="caste":
		key ="History/Class 12/Ncert Questions/kinship,caste and class early societies ncert.pdf"
	
	elif questions=="gandhi":
		key = "History/Class 12/Ncert Questions/mahatma Gandhi.pdf"

	elif questions == "peasants":
		key = "History/Class 12/Ncert Questions/Peasants, zamindars and state agaraian society-ncert.pdf"
	
	elif questions == "rebels":
		key = "History/Class 12/Ncert Questions/Rebels and raj-ncert.pdf"	
	
	elif questions=="beliefs":
		key ="History/Class 12/Ncert Questions/Thinkers, beliefs and buildings ncert.pdf"
	
	elif questions=="eyes":
		key = "History/Class 12/Ncert Questions/Through the eyes of travellers ncert.pdf"

	elif questions == "partition":
		key = "History/Class 12/Ncert Questions/UNDERSTANDING PARTITION.pdf"
	
	
	
	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)
#################################################################################################################################

if __name__ == '__main__':	
	app.run()
