$(function(){

// 최초실행 ------------------------------------------------------------------------------------

    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,65,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

    let s_data="";
    for(i=0; i<no.length; i++){
        s_data += "<tr id='"+no[i]+"'>";
        s_data += "<td><input type='checkbox' name='Chk' class='Chk value='"+no[i]+"'></td>";
        s_data += "<td>"+no[i]+"</td>";
        s_data += "<td>"+name[i]+"</td>";
        s_data += "<td>"+kor[i]+"</td>";
        s_data += "<td>"+eng[i]+"</td>";
        s_data += "<td>"+math[i]+"</td>";
        s_data += "<td>"+total[i]+"</td>";
        s_data += "<td>"+avg[i]+"</td>";
        s_data += "<td>0</td>";
        s_data += "<td><button type='button' class='dBtn()'>삭제</td>";
        s_data += "</tr>";
    }

    $("#body").html(s_data);
    // for
// 학생입력 btn-> 자료 가지고 와서 테이블 안에 넣기

// 학생삭제

    $(".dBtn").click(function(){ 
        console.log($(this).parent().parent().attr("id")); 
        if(confirm("정말 삭제하시겠습니까?"));
            $("#"+$(this).parent().parent().attr("id")).remove();
    }); //table 삭제



    $("#allChk").click(function(){
        if($(this).is("checked")==true){
            console.log("체크되었습니다");
            $(".Chk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            console.log("체크해제되었습니다");
            $(".Chk").each(function(){
                $(this).prop("checked",false);
            })
        }
    }) 

    $("#delBtn").click(function(){
        console.log("체크박스의 개수 :"+$(".Chk").length); 
        console.log("체크된 체크박스의 개수 :"+$(".Chk:checked").length);

        //ㄱ. 체크되어 있는 것이 없는경우
        if($(".Chk:checked").length<1){
            alert("선택된 항목이 있어야 삭제가 가능합니다")
            return false;
        };

        //ㄴ. 현재 체크박스가 체크되어 있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false
        }
        

        //ㄷ. 모든 체크박스 가져오기: 로직은- delBtn 눌렀을 때, 각각의 체크박스에 checked적용하여 삭제하라
        $(".Chk").each(function(){
            if($(".Chk").is(":checked")==true){
                console.log($(this).parent().attr("id"))
            }

        })
        

    });











})