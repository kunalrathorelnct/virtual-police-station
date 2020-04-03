
var c=0;
var name;
var flag=0;
var id;

var questions = ['Please tell Your Name?','What type of crime you want to report?'];


function keypress() {
    if(c!=6 && c!=8)
    {
    var w=document.getElementById("note-textarea");
w.classList.remove("notetxt");
    if (document.getElementById('note-textarea').value!=""){
        var x=document.getElementById("nextbtn");
        x.disabled=false;
        x.classList.remove("next");
        x.style.backgroundColor="#5DC8CD";
            flag=0;
    }
}
    else
    {
    var w=document.getElementById("note-textarea1");
    w.classList.remove("notetxt");
    if (document.getElementById('note-textarea1').value!=""){
        var x=document.getElementById("nextbtn");
        x.disabled=false;
        x.classList.remove("next");
        x.style.backgroundColor="#5DC8CD";
            flag=0;
    }
    }
}
function isNumberKey(evt){
    keypress();
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}
function check()
{
    if(c!=6 && c!=8)
    {
    if(document.getElementById("note-textarea").value.trim()=="")
    {
        var x=document.getElementById("nextbtn");
        x.disabled = true;
        x.classList.add("next");
        x.style.backgroundColor="#01939A";
        var w=document.getElementById("note-textarea");
w.classList.add("notetxt");
        return true;
    }
}else{
    if(document.getElementById("note-textarea1").value.trim()=="")
    {
        var x=document.getElementById("nextbtn");
        x.disabled = true;
        x.classList.add("next");
        x.style.backgroundColor="#01939A";
        var w=document.getElementById("note-textarea1");
w.classList.add("notetxt");
        return true;
    }
}
    return false;
}
/*function putrequest(dic){
    $.ajax({
        type: "PATCH",
        url: '/api/FIR/'+id+'/',
        data: dic,
        async:false,
        success: function (response) {
             console.log(response);
                 
             // window.location = response;  
            },
    });
}
*/

/*var TxtType = function(el, toRotate, period) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.period = parseInt(period, 10) || 2000;
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtType.prototype.tick = function() {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
        }

        setTimeout(function() {
        that.tick();
        }, delta);
    };
*/
    window.onload = function() {
        var w=document.getElementById("note-textarea");
w.classList.remove("notetxt");
       /* var elements = document.getElementsByClassName('typewrite');
        for (var i=0; i<elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var period = elements[i].getAttribute('data-period');
            if (toRotate) {
              new TxtType(elements[i], JSON.parse(toRotate), period);
            }
        }
        
        // INJECT CSS
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".typewrite > .wrap { border-right: 0.12em solid #fff}";
        document.body.appendChild(css);*/
    };
    /*speech synthesis utterance voivces[1] me male voice hai*/
    /*function say(m) {
        var msg = new SpeechSynthesisUtterance();
        var voices = window.speechSynthesis.getVoices();
        msg.voice=voices[1];
        //msg.voice = speechSynthesis.getVoices().filter(function(voice) { return voice.name == 'Whisper'; })[0];
        msg.voiceURI = "native";
        msg.volume = 1;
        msg.rate = 1;
        msg.pitch = 0.8;
        msg.text = m;
        msg.lang = 'en-US';
        speechSynthesis.speak(msg);
      }*/


      var timesRun=0,interval;
      function displayNextImage() {
          timesRun+=1;
          if(timesRun==20)
          clearInterval(interval);
        x = (x === images.length - 1) ? 0 : x + 1;
        document.getElementById("policepic").src = images[x];
    }

    function displayPreviousImage() {
        x = (x <= 0) ? images.length - 1 : x - 1;
        document.getElementById("policepic").src = images[x];
    }

    function startTimer() {
        interval=setInterval(displayNextImage, 150);
    }

    var images = [], x = -1;
    images[0] = "background.png";
    images[1] = "background2.png";
    images[2] = "background3.png";
    images[3] = "background4.png";
    var k = 0;
var txt = questions[c];
var speed = 130;

function typeWriter() {
  if (k< txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(k);
    k++;
    setTimeout(typeWriter, speed);
  }
}
    function next()
    {
        if(check())
        return;
        document.getElementById('demo').innerHTML = "";
        timesRun=0;
        startTimer();
        typeWriter();
     responsiveVoice.speak(txt,"US English Male");
        var x=document.getElementById("nextbtn");
        x.disabled = true;
        x.classList.add("next");
        x.style.backgroundColor="#01939A";
        c++;
        if(c==1)
        {
    name=document.getElementById("note-textarea").value;
    document.getElementById("l1").innerHTML="Name:"+name;
        }
        else if(c==2)
        {
    var type_of_crime=document.getElementById("note-textarea").value;
    document.getElementById("l2").innerHTML="Title:"+type_of_crime;

    /*function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    $.ajax({
        type: "POST",
        url: '/api/FIR/',
        data: {'name_of_victim':name,'type_of_crime':type_of_crime},
        async:false,
        success: function (response) {
             console.log(response);
             id = response.id;
             console.log(id);      
             // window.location = response;
                
            },
    });
    $.ajax({
        type    : "get",
        url     : '/api/question/?id='+id+'&type=list',       
        success : function(data)
        {   
            console.log(data)
            questions=data;
            console.log(questions);
        $('#demo').val(data);
        }
    });*/

        }
        
        else if(c==3)
        {
            var x=document.getElementById("note-textarea").value;
            /*var g = document.createElement("TEXTAREA"); 
            var f = document.createTextNode(x); */
              z=document.getElementById("l5txt");
              z.innerHTML="<textarea rows='6' id='newtxt' disabled></textarea>";
            /*g.appendChild(f); 
            document.body.appendChild(g);  */
            document.getElementById("newtxt").innerHTML=x;
            document.getElementById("newtxt").style.width="70%";

        document.getElementById("l6").innerHTML="Description:";
       /* putrequest({'description_of_incidence':x});*/
    //     $.ajax({
    //     type: "PUT",
    //     url: '/api/FIR/'+id+'/',
    //     data: {'description_of_incidence':x},
    //     async:false,
    //     success: function (response) {
    //          console.log(response);
    //          id = response.id;
    //          console.log(id);      
    //          // window.location = response;
                
    //         },
    // });
        }
        else if(c==4)
        {
    var x=document.getElementById("note-textarea").value;
    document.getElementById("l7").innerHTML="Place of occurence:"+x;
    document.getElementById("l9").innerHTML="Date of occurence:"+"<input id='time' type='datetime-local' required/>";
    /*putrequest({'location_of_crime':x});*/

        }
        
        /*else if(c==5)
        {
            document.getElementById("note-textarea").disabled=true;
    

             
    }*/
    else if(c==5)
        {
            var x=document.getElementById("note-textarea").value;
              z=document.getElementById("l10");
              z.innerHTML="Identified Accused:"+x;
        }
        else if(c==6)
        {
            /*document.getElementById("note-textarea").disabled=false;*/
            time = document.getElementById('time').value;
            console.log(time);
            var x=document.getElementById("note-textarea").value;
            document.getElementById("l8").innerHTML="Witness-details:"+x;
            document.getElementById( "note-textarea").style.display="none";
            document.getElementById("chng").innerHTML="<textarea id='note-textarea1' placeholder='Enter 10 digit number' rows='6' onkeypress='return isNumberKey(event)' class='notetxt' maxlength='10' minlength='10'></textarea>";
           /* putrequest({'datetime_of_crime':time+'Z'});*/


        }
        
        else if(c==7)
        {
            console.log("true");
            var w=document.getElementById("note-textarea1");
            w.classList.remove("notetxt");
            var x=document.getElementById("note-textarea1").value;
            if(x.length<10)
            {
        var x=document.getElementById("nextbtn");
        x.disabled=true;
        x.classList.add("next");
        var w=document.getElementById("note-textarea1");
w.classList.add("notetxt");
        c--;
        return;
            }
    document.getElementById("l3").innerHTML="Phone No:"+x;
    
            document.getElementById( "note-textarea1").style.display="none";
            document.getElementById("chng").innerHTML="<textarea id='note-textarea' placeholder='Create a new note by typing or using voice recognition.' rows='6' class='notetxt' onkeypress='keypress()'></textarea>";
            var w=document.getElementById("note-textarea");
            w.classList.remove("notetxt");
        }
        else if(c==8)
        {
            
            var x=document.getElementById("note-textarea").value;
            document.getElementById("l4").innerHTML="Address:"+"<textarea rows='3' id='newtxt1'></textarea>";
            document.getElementById('newtxt1').innerHTML = x;
            document.getElementById("newtxt1").style.width="70%";
            document.getElementById( "note-textarea").style.display="none";
            document.getElementById("chng").innerHTML="<textarea id='note-textarea1' placeholder='Enter 12 digit number.' rows='6' onkeypress='return isNumberKey(event)' class='notetxt' maxlength='12' minlength='12'></textarea>";
            /*putrequest({'address':x});    */    
         }
        else if(c==9)
        {
            console.log("true");
            var x=document.getElementById("note-textarea1").value;
            if(x.length<12)
            {
        var x=document.getElementById("nextbtn");
        x.disabled=true;
        x.classList.add("next");
        var w=document.getElementById("note-textarea1");
w.classList.add("notetxt");
        c--;
        return;
            }
            document.getElementById("l5").innerHTML="Aadhar No:"+x;
            document.getElementById( "note-textarea1").style.display="none";
            document.getElementById("chng").innerHTML="<textarea id='note-textarea' placeholder='Create a new note by typing or using voice recognition.' rows='6' class='notetxt' onkeypress='keypress()'></textarea>";
            var w=document.getElementById("note-textarea");
            w.classList.remove("notetxt");
            /*putrequest({'aadhar_no':x})*/
                document.getElementById('l11').innerHTML = "Document:"+"<input type='file' onchange='readURL(this);' />";

                z=document.getElementById("l7btn");
              z.innerHTML="<input type='submit' id='newbtn' value='submit'>";
              document.getElementById("newbtn").style.width="40%";
              document.getElementById("newbtn").style.backgroundColor="#5DC8CD";
              document.getElementById("newbtn").style.height="50px";
              document.getElementById("newbtn").style.color="#fff";
              document.getElementById("start-record-btn").disabled=true;
              document.getElementById("pause-record-btn").disabled=true;
              document.getElementById("note-textarea").disabled=true;
              document.getElementById("start-record-btn").classList.add("next");
              document.getElementById("start-record-btn").style.backgroundColor="#01939A";
              document.getElementById("pause-record-btn").classList.add("next");
              document.getElementById("pause-record-btn").style.backgroundColor="#01939A";
                document.getElementById("newbtn").onclick=function()
                {
                    window.location.href = "/firview/"+id;
                    return false;
                }
    
        }
        if(c!=6 && c!=8)
        document.getElementById("note-textarea").value="";
        flag=0;        // x.classList.add("next");
        // x.style.backgroundColor="#01939A";
        console.log(c);
}
function stop()
{
var x=document.getElementById("nextbtn");
x.disabled=false;
x.classList.remove("next");
x.style.backgroundColor="#5DC8CD";
}
