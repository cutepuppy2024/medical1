$(function(){

    // 최초데이터 불러오기
    $.ajax({
        url:"json/stu_score.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            alert("데이터 가져오기 성공")
            console.log(data)
            s_count = data.length;

            let htmlData = "";
            for(i=0; i<10; i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'><</td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>"+data[i].rank+"</td>";
                htmlData += "<td><button class='delBtn'>삭제</td>";
                htmlData += "</tr>"; 
            }// for

            $("#body").html(htmlData);
        },
        error:function(){
            alert("ajax 실패")
        }
    });// ajax

    // 검색버튼 클릭
    $("#searchBtn").click(function(){
        if($("#s_word").val().length<1){
            alert("검색할 학생이름을 입력하셔야 가능합니다.");
            return false;
        }

        let s_word = $("#s_word").val();
        console.log("검색어 :"+s_word);

        // 최초 데이터 불러와 검색하기
        $.ajax({
            url:"json/stu_score.json",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                alert("데이터 가져오기 성공");
                console.log(data)
                // 홍길동.indexOf('홍')
                if(data[i].name.indexOf(s_word)!= -1){
                    htmlData += "<tr id='"+data[i].no+"'>";
                    htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                    htmlData += "<td>"+data[i].no+"</td>";
                    htmlData += "<td>"+data[i].name+"</td>";
                    htmlData += "<td>"+data[i].kor+"</td>";
                    htmlData += "<td>"+data[i].eng+"</td>";
                    htmlData += "<td>"+data[i].math+"</td>";
                    htmlData += "<td>"+data[i].total+"</td>";
                    htmlData += "<td>"+data[i].avg+"</td>";
                    htmlData += "<td>"+data[i].rank+"</td>";
                    htmlData += "<td><button class='delBtn'>삭제</td>";
                    htmlData += "</tr>"; 
                }// if
                $("#body").html(htmlData);
            },
            error:function(){
                alert("ajax 실패");
            }
        });// ajax
    }); //검색 완료

    // 학생입력버튼 클릭
    $("#writeBtn").click(function(){
        if($(".stuChk:checked").length>=1){
            alert("학생입력을 하시려면 체크를 해제하셔야 가능합니다. \n자동체크 해제합니다.");
            // 체크모두 해제
            $(".stuChk:checked").each(function(){
                $(this).prop("checked",false);
            });
            return false
        }

        $(".p_all").css("display","block")
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    });

    // 학생입력취소버튼 클릭
    $("calcelBtn").click(function(){
        $(".p_all").css("display","none");
        //초기화
        $("#id").val(""); // ?
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");    
    });

    // 학생수정버튼 클릭
    $("modifyBtn").click(function(){
        console.log("체크박스에서 체크된 개수 :"+$(".stuChk:checked").length);

        if($(".stuChk:checked").length != 1){
            alert("학생 1명만 선택하셔야 수정이 가능합니다.")
        }
        // 선택된 체크의 데이터 가져오기
        o_id = $(".stuChk:checked").parent();
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text();
        o_eng = o_id.next().next().next().next().text();
        o_math = o_id.next().next().next().next().next().text(); 

        console.log("학번 :"+o_id.next().text())

        // 수정창열고 타이틀 변경
        $(".p_all").css("display","block");
        $("#name").prop("readonly",true);
        $(".p_main h2").text("학생성적수정")

        // 데이터 값 가져오기
        $("#id").val(o_no);
        $("#name").val(o_name);
        $("#kor").val(o_kor);
        $("#eng").val(o_eng);
        $("#math").val(o_math);
    })

    // 학생입력, 수정 확인 버튼
    $("confirmBtn").on("click",function(){
        if($("#id").val()==""){
            console.log("이름 :"+$("name").val());
            alert("test")

            //공백확인
            if(("#name").val().length<2){
                alert("이름을 입력하셔야 등록이 가능합니다.");
                $("name").focus();
                return false;
            }

            // 번호 생성은 DB에서 자동으로 부여
            console.log("confirmBtn s_count:"+s_count);
            s_count = s_count +1
            console.log("번호 :"+s_count);
            let i_name = $("#name").val();
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(2);

            //table tr추가
            let htmlData = "";
            htmlData += "<tr id='"+s_count+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'></td>";
            htmlData += "<td>"+s_count+"</td>";
            htmlData += "<td>"+i_name+"</td>";
            htmlData += "<td>"+i_kor+"</td>";
            htmlData += "<td>"+i_eng+"</td>";
            htmlData += "<td>"+i_math+"</td>";
            htmlData += "<td>"+i_total+"</td>";
            htmlData += "<td>"+i_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";

            $("body").html(htmlData);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }else{ // value 값이 있는 경우 -> 수정
            //alert("학생성적수정창 클릭");
            let o_no = $("#id").val();
            let o_name = $("#name").val();
            let o_kor = Number($("#kor").val());
            let o_eng = Number($("#eng").val());
            let o_math = Number($("#math").val());
            let o_total = i_kor+i_eng+i_math;
            let o_avg = (i_total/3).toFixed(2);

            console.log("id :"+o_no);
            console.log("kor :"+o_kor);
            console.log("eng :"+o_eng);
            console.log("math :"+o_math);

            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += "<td>"+o_no+"</td>";
            htmlData += "<td>"+o_name+"</td>";
            htmlData += "<td>"+o_kor+"</td>";
            htmlData += "<td>"+o_eng+"</td>";
            htmlData += "<td>"+o_math+"</td>";
            htmlData += "<td>"+o_total+"</td>";
            htmlData += "<td>"+o_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";

            $("#"+o_no).html(htmlData);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        }
    }); // 학생입력, 수정 확인 버튼 완료

    // 전체선택, 취소
    $("allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false)
            })
        }
    }); // 전체선택,취소 완료

    // table의 삭제버튼 
    $(document).on("click",".delBtn",function(){
        console.log($(this).parent.parent.attr("id"))
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });// talbe 삭제

    // 하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        // 체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.")
            return false;
        }// 삭제 if

        // 현재 체크박스가 체크되어 있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false
        }
        // 모든체크박스 가져와 삭제
        $("#allChk").each(function(){
            if((this).is("checked")==true){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        })// 삭제완료
    })


}); //jquery