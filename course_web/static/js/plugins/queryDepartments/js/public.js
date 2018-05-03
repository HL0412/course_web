(function() {
    $(".prodepartmentSelAll").click(function(event) {
        var $box = $(".departmentdepartmentAll"),
            $body = $("body");
        if ($body.data("departmentsAll") == null) {
            sendAlldepartmentsAjax();
        }
        $(this).select();
        $(".departmentdepartment").hide();
        $box.hide();
        $("#dimdepartmentQuery").hide();
        var o2 = $(this).offset();
        var l2 = o2.left;
        var t2 = o2.top;
        var h2 = $(this).height();
        $box.css("top", t2 + h2 + 15).css("left", l2).toggle();
        $box.click(function(event) {
            event.stopPropagation();
        });
        event.stopPropagation();
        $("html").click(function() {
            $box.hide();
        });
        $("input.prodepartmentSelAll").removeClass("current2");
        $(this).addClass("current2");
        $box.find(".tabs").find("a").removeClass("current");
        $box.find(".tabs").find("a[tb=departmentAll]").addClass("current");
        $box.find(".con").children().hide();
        $box.find(".con").find(".departmentAll").show();
        if ($body.data("alldepartments") == null) {
            sendAlldepartmentAjax();
        }
        if ($body.data("allCountys") == null) {
            sendAllCountiesAjax();
        }
        $box.find(".tabs").find("a").click(function() {
            if ($(this).attr("tb") == "departmentAll" && $(".departmentAll .list .current").val() == null) {
                return;
            };
            if ($(this).attr("tb") == "countyAll" && $(".departmentAll .list .current").val() == null && $(".hotdepartmentAll .list .current").val() == null) {
                return;
            };
            $box.find(".tabs").find("a").removeClass("current");
            $(this).addClass("current");
            var tb = $(this).attr("tb");
            $box.find(".con").children().hide();
            $box.find(".con").find("." + tb).show();
        });
    });
})();

(function() {
    var clkIndex;
    var currentClass;
    var alldepartments;
    var alldepartments;
    var allCountys;
    var thisObj;
    var dimdepartmentDiv = "<div id='dimdepartmentQuery'><ul></ul></div>";
    $("body").append(dimdepartmentDiv);
    $("body").delegate(".prodepartmentQuery,.prodepartmentQueryAll", ($.browser.opera ? "keypress": "keyup"),
        function(event) {
            if ($("#dimdepartmentQuery:visible").size() == 0) {
                $(".backifname").hide();
            }
            $(".departmentdepartment").hide();
            $(".departmentdepartmentAll").hide();
            if ($(this).hasClass("prodepartmentQueryAll"))
            {
                if ($("body").data("alldepartments") == null) {
                    sendAlldepartmentAjax();
                }
                if ($("body").data("departmentsAll") == null) {
                    sendAlldepartmentsAjax();
                }
                if ($("body").data("allCountys") == null) {
                    sendAllCountiesAjax();
                }
                currentClass = "prodepartmentQueryAll";
                clkIndex = $("body").find(".prodepartmentQueryAll").index(this);
                alldepartments = $("body").data("departmentsAll");
                alldepartments = $("body").data("alldepartments");
                allCountys = $("body").data("allCountys");
                thisObj = $(this);
            }
            if ($(this).hasClass("prodepartmentQuery"))
            {
                if ($("body").data("allExistdepartments") == null) {
                    senddepartmentAjax();
                }
                if ($("body").data("allExistdepartments") == null) {
                    senddepartmentsAjax();
                }
                if ($("body").data("allExistCountys") == null) {
                    sendCountiesAjax();
                }
                currentClass = "prodepartmentQuery";
                clkIndex = $("body").find(".prodepartmentQuery").index(this);
                alldepartments = $("body").data("allExistdepartments");
                alldepartments = $("body").data("allExistdepartments");
                allCountys = $("body").data("allExistCountys");
                thisObj = $(this);
            }
            lastKeyPressCode = event.keyCode;
            switch (lastKeyPressCode) {
                case 40:
                    $("#dimdepartmentQuery").trigger("selNext");
                    return false;
                    break;
                case 38:
                    $("#dimdepartmentQuery").trigger("selPrev");
                    return false;
                    break;
                case 13:
                    $("#dimdepartmentQuery").trigger("enter");
                    return false;
                    break;
            }
            v = $.trim($(this).val());
            if (v == "" || v == null) {
                return false;
            }
            $(".departmentdepartment").hide();
            var o = $(this).offset();
            var l = o.left;
            var t = o.top;
            var w = $(this).width();
            var h = $(this).height();
            var htmlArr = [];
            var autoWidth;
            for (i = 0; i < allCountys.length; i++) {
                if (v.toUpperCase() === allCountys[i].pinYinChar.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + allCountys[i].departmentId + " departmentId=" + allCountys[i].departmentId + " countyId=" + allCountys[i].id + ">" + allCountys[i].departmentName + "-" + allCountys[i].areaName + " (<span style='color:red'>" + v.toUpperCase() + "</span>" + allCountys[i].pinYinChar.substring(v.length, allCountys[i].pinYinChar.length) + ")</a></li>";
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYinChar).length ? (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYinChar).length: autoWidth;
                    continue;
                };
                if (v === allCountys[i].areaName.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + allCountys[i].departmentId + " departmentId=" + allCountys[i].departmentId + " countyId=" + allCountys[i].id + ">" + allCountys[i].departmentName + "-" + "<span style='color:red'>" + v + "</span>" + allCountys[i].areaName.substring(v.length, allCountys[i].areaName.length) + " (" + allCountys[i].pinYinChar + ")</a></li>";
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYinChar).length ? (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYinChar).length: autoWidth;
                    continue;
                };
                if (v.toLowerCase() === allCountys[i].pinYin.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + allCountys[i].departmentId + " departmentId=" + allCountys[i].departmentId + " countyId=" + allCountys[i].id + ">" + allCountys[i].departmentName + "-" + allCountys[i].areaName + " (<span style='color:red'>" + v.toLowerCase() + "</span>" + allCountys[i].pinYin.substring(v.length, allCountys[i].pinYin.length) + ")</a></li>"
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYin).length ? (allCountys[i].departmentName + allCountys[i].areaName + allCountys[i].pinYin).length: autoWidth;
                    continue;
                };
            }
            for (i = 0; i < alldepartments.departments.length; i++) {
                if (v.toUpperCase() === alldepartments.departments[i].departmentShortPY.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + alldepartments.departments[i].departmentId + " departmentId=" + alldepartments.departments[i].id + ">" + alldepartments.departments[i].name + " (<span style='color:red'>" + v.toUpperCase() + "</span>" + alldepartments.departments[i].departmentShortPY.substring(v.length, alldepartments.departments[i].departmentShortPY.length) + ")</a></li>";
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (alldepartments.departments[i].name + alldepartments.departments[i].departmentShortPY).length ? (alldepartments.departments[i].name + alldepartments.departments[i].departmentShortPY).length: autoWidth;
                    continue;
                };
                if (v === alldepartments.departments[i].name.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + alldepartments.departments[i].departmentId + " departmentId=" + alldepartments.departments[i].id + "><span style='color:red'>" + v + "</span>" + alldepartments.departments[i].name.substring(v.length, alldepartments.departments[i].name.length) + " (" + alldepartments.departments[i].departmentShortPY + ")</a></li>";
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (alldepartments.departments[i].name + alldepartments.departments[i].departmentShortPY).length ? (alldepartments.departments[i].name + alldepartments.departments[i].departmentShortPY).length: autoWidth;
                    continue;
                };
                if (v.toLowerCase() === alldepartments.departments[i].departmentPinyin.substring(0, v.length)) {
                    htmlArr[htmlArr.length] = "<li><a class='alldepartmentClass' href='javascript:' departmentId=" + alldepartments.departments[i].departmentId + " departmentId=" + alldepartments.departments[i].id + ">" + alldepartments.departments[i].name + " (<span style='color:red'>" + v.toLowerCase() + "</span>" + alldepartments.departments[i].departmentPinyin.substring(v.length, alldepartments.departments[i].departmentPinyin.length) + ")</a></li>"
                    if (htmlArr.length > 9) {
                        break;
                        return false;
                    }
                    autoWidth = autoWidth < (alldepartments.departments[i].name + alldepartments.departments[i].departmentPinyin).length ? (alldepartments.departments[i].name + alldepartments.departments[i].departmentPinyin).length: autoWidth;
                    continue;
                };
            };
            if (htmlArr == "" || htmlArr == null) {
                $("#dimdepartmentQuery ul").html("<li class='none'>对不起,没有找到该城市</li>");
                return false;
            } else {
                $("#dimdepartmentQuery ul").html(htmlArr.join("")).find("li:first").addClass("current");
            };
            if (autoWidth < 200) {
                autoWidth = 200;
            }
            $("#dimdepartmentQuery").css("width", autoWidth).css("top", t + h - 1).css("left", l).show();
            $(".backifname").show();
            $("html").click(function() {
                $("#dimdepartmentQuery").hide();
                $(".backifname").hide();
            });
        });
    $("body").delegate("#dimdepartmentQuery li", "hover",
        function() {
            $(this).addClass("current").siblings().removeClass("current");
        },
        function() {
            $(this).removeClass("current");
        });
    $("#dimdepartmentQuery").delegate("", "selNext",
        function() {
            var next = $(this).find("li.current").next();
            if (next.size() > 0) {
                next.addClass("current").siblings().removeClass("current");
            }
            else {
                $("#dimdepartmentQuery li").removeClass("current").first().addClass("current");
            };
        });
    $("#dimdepartmentQuery").delegate("", "selPrev",
        function() {
            var prev = $(this).find("li.current").prev();
            if (prev.size() > 0) {
                prev.addClass("current").siblings().removeClass("current");
            }
            else {
                $("#dimdepartmentQuery li").removeClass("current").last().addClass("current");
            };
        });
    $("#dimdepartmentQuery").delegate("", "enter",
        function(event) {
            var cur = $(this).find("li.current");
            if (cur.size() > 0) {
                cur.find("a").trigger("click");
            };
        });
    $("body").delegate("#dimdepartmentQuery li a.alldepartmentClass", "click",
        function() {
            var vm = $(this).text();
            var departmentId = $(this).attr("departmentId");
            var departmentId = $(this).attr("departmentId");
            var countyId = $(this).attr("countyId");
            var departmentName;
            var departmentName;
            var rtn;
            for (i = 0; i < alldepartments.length; i++) {
                if (alldepartments[i].id == departmentId) {
                    departmentName = alldepartments[i].departmentName;
                };
            }
            for (i = 0; i < alldepartments.departments.length; i++) {
                if (alldepartments.departments[i].id == departmentId) {
                    departmentName = alldepartments.departments[i].name;
                }
            }
            if (currentClass == "prodepartmentQueryAll") {
                $("body").data("pAllId", departmentId);
                $("body").data("cAllId", departmentId);
                $("body").data("aAllId", countyId);
                $("body").data("pAllName", departmentName);
                $("body").data("nameOfdepartmentAll", departmentName);
            }
            if (currentClass == "prodepartmentQuery") {
                $("body").data("pId", departmentId);
                $("body").data("cId", departmentId);
                $("body").data("aId", countyId);
                $("body").data("pName", departmentName);
                $("body").data("nameOfdepartment", departmentName);
            }
            vm = vm.split("(");
            countyName = $.trim(vm[0]);
            if (countyId == null || countyName == departmentName)
            {
                if (currentClass == "prodepartmentQuery")
                {
                    thisObj.trigger("click");
                    counties = [];
                    var j = 0;
                    $.each(allCountys,
                        function(i, county) {
                            if (county.departmentId == departmentId) {
                                counties[j++] = county;
                            }
                        });
                    countyTotalPage = Math.ceil(counties.length / p_pageSize);
                    $(".departmentdepartment").find(".tabs").find("a").removeClass("current");
                    $(".departmentdepartment .tabs").find("#county").addClass("current");
                    $(".con .department .list a").removeClass("current");
                    $(".departmentdepartment").find(".con").children().hide();
                    $(".departmentdepartment").find(".con").find(".county").show();
                    $(".con .departmentAll .list a").removeClass("current");
                    countyPage(1);
                }
                else if (currentClass == "prodepartmentQueryAll")
                {
                    thisObj.trigger("click");
                    countiesAll = [];
                    var j = 0;
                    $.each(allCountys,
                        function(i, county) {
                            if (county.departmentId == departmentId && county.areaName != departmentName) {
                                countiesAll[j++] = county;
                            }
                        });
                    countyTotalPageAll = Math.ceil(countiesAll.length / p_pageSize);
                    $(".departmentdepartmentAll").find(".tabs").find("a").removeClass("current");
                    $(".departmentdepartmentAll .tabs").find("#countyAll").addClass("current");
                    $(".con .departmentAll .list a").removeClass("current");
                    $(".departmentdepartmentAll").find(".con").children().hide();
                    $(".departmentdepartmentAll").find(".con").find(".countyAll").show();
                    $(".con .departmentAll .list a").removeClass("current");
                    allCountyPage(1);
                }
            }
            else
            {
                rtn = departmentName + "-" + countyName;
                if (currentClass == "prodepartmentQueryAll")
                {
                    $("body").find(".prodepartmentQueryAll").eq(clkIndex).val(rtn);
                    $("body").find(".prodepartmentQueryAll").eq(clkIndex).trigger("change");
                    $(".departmentdepartmentAll").find(".tabs").find("a").removeClass("current");
                    $(".departmentdepartmentAll").find(".tabs").find("a[tb=hotdepartmentAll]").addClass("current");
                    $(".departmentdepartmentAll .con .list a").removeClass("current");
                    $(".departmentdepartmentAll .con .list a input").removeClass("current");
                }
                if (currentClass == "prodepartmentQuery")
                {
                    $("body").find(".prodepartmentQuery").eq(clkIndex).val(rtn);
                    $("body").find(".prodepartmentQuery").eq(clkIndex).trigger("change", [departmentId, countyId]);
                    $(".departmentdepartment").find(".tabs").find("a").removeClass("current");
                    $(".departmentdepartment").find(".tabs").find("a[tb=hotdepartment]").addClass("current");
                    $(".departmentdepartment .con .list a").removeClass("current");
                    $(".departmentdepartment .con .list a input").removeClass("current");
                }
            }
            $("#dimdepartmentQuery").hide();
            $(".backifname").hide();
            return false;
        });
    $(".nomarl").live("focus",
        function() {
            var ov = $.trim($(this).attr("ov"));
            var val = $.trim($(this).val());
            $(this).css({
                "color": "#000"
            });
            if (val == ov) {
                $(this).val("");
            }
        });
    $(".nomarl").live("blur",
        function() {
            var ov = $.trim($(this).attr("ov"));
            var val = $.trim($(this).val());
            if (val == "" || val == ov) {
                $(this).val(ov).css({
                    "color": "#aaa"
                });
            }
        });
})();

function senddepartmentsAjax() {
    $.ajax({
        type: "get",
        url: '/static/js/plugins/querydepartment/js/queryAlldepartments.js',
        async: false,
        dataType: "json",
        success: function(data) {
            departments = data.departments;
            $("body").data("allExistdepartments", data);
            viewHotdepartments();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert("网络繁忙，请稍后再试！");
        }
    });
}


function viewHotdepartments() {
    $.each(departments,function(i, department) {
        if (department.hotdepartment) {
            $(".hotdepartment .list ul").append("<li><a><input type='button' style='background:none;border:0px;cursor: pointer;' onclick=hotdepartmentAddrInput(\'" + department.departmentId + "," + department.id + "," + department.name + "\') id='" + department.id + "' value='" + department.name + "'></a></li>");
        }
    });
}
$(".department .pre a").bind('click',function() {
    var departmentPage = parseInt($('#departmentPage').html());
    if (departmentPage == 1) {
        return;
    }
    viewdepartment(departmentPage - 1);
});
$(".department .pre a").bind('click',function() {
    var departmentPages = parseInt($('#departmentPage').html());
    if (departmentPages == 1) {
        return;
    }
    departmentPage(departmentPages - 1);
});
$(".county .pre a").bind('click',function() {
    var countyPages = parseInt($('#countyPage').html());
    if (countyPages == 1) {
        return;
    }
    countyPage(countyPages - 1);
});
$(".department .next a").bind('click',function() {
    var departmentPage = parseInt($('#departmentPage').html());
    departmentTotalPage = countdepartmentPages();
    if (departmentPage == departmentTotalPage) {
        return;
    }
    viewdepartment(departmentPage + 1);
});
$(".department .next a").bind('click',function() {
    if ($(this).hasClass("can")) {
        var departmentPages = parseInt($('#departmentPage').html());
        departmentPage(departmentPages + 1);
    }
});
$(".county .next a").bind('click',function() {
    if ($(this).hasClass("can")) {
        var countyPages = parseInt($('#countyPage').html());
        countyPage(countyPages + 1);
    }
});

function countdepartmentPages() {
    departmentTotalPage = Math.ceil(departments.length / p_pageSize);
    return departmentTotalPage;
}

function viewdepartment(page) {
    $(".department .list ul li").remove();
    if (page == 1) {
        $(".department .pre a").removeClass("can");
        $(".department .next a").addClass("can");
    } else {
        $(".department .pre a").addClass("can");
        $(".department .next a").addClass("can");
    }
    var end;
    var start;
    if (page == departmentTotalPage) {
        start = (page - 1) * p_pageSize;
        end = departments.length;
        $(".department .next a").removeClass("can");
    } else {
        start = (page - 1) * p_pageSize;
        end = start + p_pageSize;
    }
    for (var i = start; i < end; i++) {
        var p_id = departments[i].id;
        var p_name = departments[i].departmentName;
        if (departments[i].departmentName == '内蒙古自治区') {
            p_name = '内蒙古';
        } else if (departments[i].departmentName == '黑龙江省') {
            p_name = '黑龙江';
        } else {
            p_name = departments[i].departmentName.substr(0, 2);
        }
        var li = $('<li><a style="background: none repeat scroll 0% 0% transparent; border: 0px none;" href="javascript:onclick=viewdepartments(' + i + ');" id="' + p_id + '">' + p_name + '</a></li>');
        $(".department .list ul").append(li);
    }
    $(".department .list #departmentPage").remove();
    $(".department .list").append("<label id='departmentPage' style='display:none;'>" + page + "</label>");
}

function viewdepartments(i) {
    proId = departments[i].id;
    $("body").data("pName", departments[i].departmentName);
    $("body").data("pId", proId);
    departments = [];
    var j = 0;
    $.each(departments,
        function(i, department) {
            if (department.departmentId == proId) {
                departments[j++] = department;
            }
        });
    departmentTotalPage = Math.ceil(departments.length / p_pageSize);
    $(".departmentdepartment").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartment .tabs").find("#department").addClass("current");
    $(".con .department .list a").removeClass("current");
    $(".con .department .list a[id='" + proId + "']").addClass("current");
    $(".departmentdepartment").find(".con").children().hide();
    $(".departmentdepartment").find(".con").find(".department").show();
    departmentPage(1);
}

function departmentPage(page) {
    $(".department .list ul li").remove();
    $(".departmentAll .list ul li").remove();
    if (page == 1) {
        $(".department .pre a").removeClass("can");
    } else {
        $(".department .pre a").addClass("can");
    }
    var start;
    var end;
    if (page <= 1) {
        page = 1;
        $(".department .pre a").removeClass("can");
        $(".department .next a").addClass("can");
    }
    if (departmentTotalPage == 1) {
        $(".department .next a").removeClass("can");
        $(".department .pre a").removeClass("can");
    }
    if (page >= departmentTotalPage) {
        page = departmentTotalPage;
        $(".department .next a").removeClass("can");
        start = (page - 1) * p_pageSize;
        end = departments.length;
    } else if (page == 1) {
        start = (page - 1) * p_pageSize;
        end = start + p_pageSize;
        $(".department .pre a").removeClass("can");
        $(".department .next a").addClass("can");
    } else {
        start = (page - 1) * p_pageSize;
        end = start + p_pageSize;
        $(".department .next a").addClass("can");
        $(".department .pre a").addClass("can");
    }
    for (var i = start; i < end; i++) {
        var c_id = departments[i].id;
        var departmentName = departments[i].name.substr(0, 4);
        var li = $('<li><a href="javascript:onclick=viewCounties(' + i + ')" id="' + c_id + '">' + departmentName + '</a></li>');
        $(".department .list ul").append(li);
    }
    $(".department .list #departmentPage").remove();
    $(".department .list").append("<label id='departmentPage' style='display:none;'>" + page + "</label>");
}

function viewCounties(i) {
    departmentId = departments[i].id;
    $("body").data("cId", departmentId);
    var nameOfdepartment = $.trim(departments[i].name);
    $("body").data("nameOfdepartment", nameOfdepartment);
    counties = [];
    var j = 0;
    $.each(areas,
        function(i, county) {
            if (county.departmentId == departmentId) {
                counties[j++] = county;
            }
        });
    countyTotalPage = Math.ceil(counties.length / p_pageSize);
    $(".departmentdepartment").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartment .tabs").find("#county").addClass("current");
    $(".con .department .list a").removeClass("current");
    $(".con .department .list a[id='" + departmentId + "']").addClass("current");
    $(".departmentdepartment").find(".con").children().hide();
    $(".departmentdepartment").find(".con").find(".county").show();
    countyPage(1);
}

function countyPage(page) {
    var nameValue = $("input.current1").attr("name");
    var nameOfdepartment = $("body").data("pName");
    var departmentCurName = $("body").data("nameOfdepartment");
    $("input.current1").removeClass("iGrays");
    $("input.current1").val(nameOfdepartment + "-" + departmentCurName);
    $(".county .list ul li").remove();
    if (page == 1) {
        $(".county .pre a").removeClass("can");
    } else {
        $(".county .pre a").addClass("can");
    }
    var start;
    var end;
    if (page <= 1) {
        page = 1;
        $(".county .pre a").removeClass("can");
        $(".county .next a").addClass("can");
    }
    if (countyTotalPage == 1) {
        $(".county .next a").removeClass("can");
        $(".county .pre a").removeClass("can");
    }
    if (page >= countyTotalPage) {
        page = countyTotalPage;
        $(".county .next a").removeClass("can");
        start = (page - 1) * p_pageSize;
        end = counties.length;
    } else if (page == 1) {
        start = (page - 1) * p_pageSize;
        end = start + p_pageSize;
        $(".county .pre a").removeClass("can");
        $(".county .next a").addClass("can");
    } else {
        start = (page - 1) * p_pageSize;
        end = start + p_pageSize;
        $(".county .next a").addClass("can");
        $(".county .pre a").addClass("can");
    }
    for (var i = start; i < end; i++) {
        var c_id = counties[i].id;
        var countyName = counties[i].areaName.substr(0, 4);;
        var li = $('<li><a href="javascript:onclick=addrInput(' + i + ')" id="' + c_id + '">' + countyName + '</a></li>');
        $(".county .list ul").append(li);
    }
    $(".county .list #countyPage").remove();
    $(".county .list").append("<label id='countyPage' style='display:none;'>" + page + "</label>");
}

function addrInput(i) {
    var countyId = $.trim(counties[i].id);
    $(".con .hotdepartment .list a input").removeClass("current");
    $(".con .hotdepartment .list a input[id='" + departmentId + "']").addClass("current");
    $(".con .county .list a").removeClass("current");
    $(".con .county .list a[id='" + countyId + "']").addClass("current");
    proId = $("body").data("pId");
    departmentId = $("body").data("cId");
    var p = null;
    $.each(departments, function(i, department) {
        if (department.id == proId) {
            p = department.departmentName;
            return false;
        }
    });
    var c = null;
    $.each(departments, function(i, department) {
        if (department.id == departmentId) {
            c = department.name;
            return false;
        }
    });
    var a = null;
    $.each(counties, function(i, county) {
        if (county.id == countyId) {
            a = county.areaName;
            return false;
        }
    });
    $("input.current1").removeClass("iGrays");
    $(".departmentdepartment").hide();
    var rtn = p + "-" + c + "-" + a;
    $("input.current1").val(rtn);
    $(".backifname").hide();
    var nameValue = $("input.current1").attr("name");
    if (nameValue == 'order.sdeptProdepartment')
    {
        $("#deptdepartmentId").val(departmentId);
        $("input[name='order.sdeptProdepartment']").trigger("change", [departmentId, countyId]);
    }
    if (nameValue == 'consignor.deptProdepartment')
    {
        $("input[name='consignor.deptProdepartment']").trigger("change", [departmentId, countyId]);
    }
    if (nameValue == 'template.sdeptProdepartment')
    {
        $("input[name='template.sdeptProdepartment']").trigger("change", [departmentId, countyId]);
    }
}
function hotdepartmentAddrInput(prodepartmentId) {
    proId = prodepartmentId.split(",")[0];
    departmentId = prodepartmentId.split(",")[1];
    var departmentCurName = prodepartmentId.split(",")[2];
    $("body").data("nameOfdepartment", departmentCurName);
    $("body").data("pId", proId);
    $("body").data("cId", departmentId);
    $.each(departments, function(i, pro) {
        if (pro.id == proId) {
            $("body").data("pName", pro.departmentName);
        }
    });
    counties = [];
    var j = 0;
    $.each(areas,
        function(i, county) {
            if (county.departmentId == departmentId) {
                counties[j++] = county;
            }
        });
    countyTotalPage = Math.ceil(counties.length / p_pageSize);
    $(".departmentdepartment").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartment .tabs").find("#county").addClass("current");
    $(".con .department .list a").removeClass("current");
    $(".con .department .list a[id='" + departmentId + "']").addClass("current");
    $(".departmentdepartment").find(".con").children().hide();
    $(".departmentdepartment").find(".con").find(".county").show();
    $(".con .departmentAll .list a").removeClass("current");
    countyPage(1);
}
var alldepartments = null;
var alldepartments = null;
var allAreas = null;
var allProId = null;
var departmentIdAll = null;
var departmentAllTotalPage = null;
var pa_pageSize = 12;
var pa_currentPage = 1;
function sendAlldepartmentAjax() {
    $.ajax({
        type: "get",
        url: '/static/js/plugins/querydepartment/js/queryAlldepartments.js',
        async: false,
        dataType: "json",
        success: function(data) {
            alldepartments = data.departments;
            $("body").data("alldepartments", alldepartments);
            viewAlldepartment(1);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert(textStatus);
        }
    });
}
function sendAlldepartmentsAjax() {
    $.ajax({
        type: "get",
        url: '/static/js/plugins/querydepartment/js/querydepartments.js',
        async: false,
        dataType: "json",
        success: function(data) {
            alldepartments = data.departments;
            $("body").data("departmentsAll", data);
            viewAllHotdepartments();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert(textStatus);
        }
    });
}
function sendAllCountiesAjax(){
    $.ajax({
        type: "get",
        url: "/static/js/plugins/querydepartment/js/queryAllAreas.js",
        async: false,
        dataType: "json",
        success: function(data) {
            allAreas = data.areas;
            $("body").data("allCountys", data.areas);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert("网络繁忙，请稍后再试！");
        }
    });
}
function viewAllHotdepartments() {
    $.each(alldepartments,function(i, department) {
        if (department.hotdepartment) {
            $(".hotdepartmentAll .list ul").append("<li><a><input type='button' style='background:none;border:0px;cursor: pointer;' onclick=hotdepartmentAddrInputAll(\'" + department.departmentId + "," + department.id + "," + department.name + "\') id='" + department.id + "' value='" + department.name + "'></a></li>");
        }
    });
}
$(".departmentAll .pre a").bind('click', function() {
    var departmentPage1 = parseInt($('#departmentPage1').html());
    if (departmentPage1 == 1) {
        return;
    }
    viewAlldepartment(departmentPage1 - 1);
});
$(".departmentAll .pre a").bind('click', function() {
    var departmentPages1 = parseInt($('#departmentPage1').html());
    if (departmentPages1 == 1) {
        return;
    }
    alldepartmentPage(departmentPages1 - 1);
});

$(".countyAll .pre a").bind('click', function() {
    var countyPages = parseInt($('#countyPage1').html());
    if (countyPages == 1) {
        return;
    }
    allCountyPage(countyPages - 1);
});

$(".departmentAll .next a").bind('click', function() {
    var departmentPage1 = parseInt($('#departmentPage1').html());
    departmentAllTotalPage = countAlldepartmentPages();
    if (departmentPage1 >= departmentAllTotalPage) {
        return;
    }
    viewAlldepartment(departmentPage1 + 1);
});

$(".departmentAll .next a").bind('click', function() {
    if ($(this).hasClass("can")) {
        var departmentPages1 = parseInt($('#departmentPage1').html());
        alldepartmentPage(departmentPages1 + 1);
    }
});

$(".countyAll .next a").bind('click', function() {
    if ($(this).hasClass("can")) {
        var countyPages = parseInt($('#countyPage1').html());
        allCountyPage(countyPages + 1);
    }
});

function countAlldepartmentPages() {
    departmentAllTotalPage = Math.ceil(alldepartments.length / pa_pageSize);
    departmentAllTotalPage = Math.ceil(1 / pa_pageSize);
    return departmentAllTotalPage;
}

function viewAlldepartment(page) {
    $(".departmentAll .list ul li").remove();
    //if (page == 1) {  //可打开所有省
    //    $(".departmentAll .pre a").removeClass("can");
    //    $(".departmentAll .next a").addClass("can");
    //} else {
    //    $(".departmentAll .pre a").addClass("can");
    //    $(".departmentAll .next a").addClass("can");
    //}
    //var end;
    //var start;
    //if (page == departmentAllTotalPage) {
    //    start = (page - 1) * pa_pageSize;
    //    end = alldepartments.length;
    //    $(".departmentAll .next a").removeClass("can");
    //} else {
    //    start = (page - 1) * pa_pageSize;
    //    end = start + pa_pageSize;
    //}
    $(".departmentAll .pre a").removeClass("can");
    $(".departmentAll .next a").removeClass("can");
    for (var i = 27; i < 28; i++) {
        var p_id = alldepartments[i].id,
            p_name = alldepartments[i].departmentName;

        if (alldepartments[i].departmentName == '内蒙古自治区') {
            p_name = '内蒙古';
        } else if (alldepartments[i].departmentName == '黑龙江省') {
            p_name = '黑龙江';
        } else {
            p_name = alldepartments[i].departmentName.substr(0, 2);
        }
        if(p_name == '四川'){
            var li = $('<li><a style="background: none repeat scroll 0% 0% transparent; border: 0px none;" href="javascript:onclick=viewAlldepartments(' + i + ');" id="' + p_id + '">' + p_name + '</a></li>');
            $(".departmentAll .list ul").append(li);
        }

    }
    $(".departmentAll .list #departmentPage1").remove();
    $(".departmentAll .list").append("<label id='departmentPage1' style='display:none;'>" + page + "</label>");
}

function viewAlldepartments(i) {
    allProId = alldepartments[i].id;
    $("body").data("pAllName", alldepartments[i].departmentName);
    $("body").data("pAllId", allProId);
    alldepartments = [];
    var j = 0;
    $.each(alldepartments,
        function(i, department) {
            //if (department.departmentId == allProId) { //可打开所有城市
            //    alldepartments[j++] = department;
            //}
            if(department.id == 'uIMcazYzTxeHdTDr+k7rilC+DzM='){
                alldepartments[j++] = department;
            }
        });
    alldepartmentTotalPage = Math.ceil(alldepartments.length / pa_pageSize);
    $(".departmentdepartmentAll").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartmentAll .tabs").find("#departmentAll").addClass("current");
    $(".con .departmentAll .list a").removeClass("current");
    $(".con .departmentAll .list a[id='" + allProId + "']").addClass("current");
    $(".departmentdepartmentAll").find(".con").children().hide();
    $(".departmentdepartmentAll").find(".con").find(".departmentAll").show();
    alldepartmentPage(1);
}

function alldepartmentPage(page) {
    $(".departmentAll .list ul li").empty();
    $(".departmentAll .list ul li").remove();
    if (page == 1) {
        $(".departmentAll .pre a").removeClass("can");
    } else {
        $(".departmentAll .pre a").addClass("can");
    }
    var start;
    var end;
    if (page <= 1) {
        page = 1;
        $(".departmentAll .pre a").removeClass("can");
        $(".departmentAll .next a").addClass("can");
    }
    if (alldepartmentTotalPage == 1) {
        $(".departmentAll .next a").removeClass("can");
        $(".departmentAll .pre a").removeClass("can");
    }
    if (page >= alldepartmentTotalPage) {
        page = alldepartmentTotalPage;
        $(".departmentAll .next a").removeClass("can");
        start = (page - 1) * pa_pageSize;
        end = alldepartments.length;
    } else if (page == 1) {
        start = (page - 1) * pa_pageSize;
        end = start + pa_pageSize;
        $(".departmentAll .pre a").removeClass("can");
        $(".departmentAll .next a").addClass("can");
    } else {
        start = (page - 1) * pa_pageSize;
        end = start + pa_pageSize;
        $(".departmentAll .next a").addClass("can");
        $(".departmentAll .pre a").addClass("can");
    }
    for (var i = start; i < end; i++) {
        var c_id = alldepartments[i].id;
        var departmentName = alldepartments[i].name.substr(0, 4);
        var li = $('<li><a href="javascript:onclick=viewAllCounties(' + i + ')" id="' + c_id + '">' + departmentName + '</a></li>');
        $(".departmentAll .list ul").append(li);
    }
    $(".departmentAll .list #departmentPage1").remove();
    $(".departmentAll .list").append("<label id='departmentPage1' style='display:none;'>" + page + "</label>");
}
function viewAllCounties(i) {
    departmentIdAll = alldepartments[i].id;
    $("body").data("cAllId", departmentIdAll);
    var departmentname = $.trim(alldepartments[i].name);
    $("body").data("nameOfdepartmentAll", departmentname);
    countiesAll = [];
    var j = 0;
    $.each(allAreas,
        function(i, countys) {
            if (countys.departmentId == departmentIdAll) {
                countiesAll[j++] = countys;
            }
        });
    countyTotalPageAll = Math.ceil(countiesAll.length / pa_pageSize);
    $(".departmentdepartmentAll").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartmentAll .tabs").find("#countyAll").addClass("current");
    $(".con .departmentAll .list a").removeClass("current");
    $(".con .departmentAll .list a[id='" + departmentIdAll + "']").addClass("current");
    $(".departmentdepartmentAll").find(".con").children().hide();
    $(".departmentdepartmentAll").find(".con").find(".countyAll").show();
    allCountyPage(1);
}

function allCountyPage(page) {
    var nameOfdepartment = $("body").data("pAllName");
    var departmentCurrentName = $("body").data("nameOfdepartmentAll");
    $("input.current2").removeClass("iGrays");
    $("input.current2").val(nameOfdepartment + "-" + departmentCurrentName);
    $(".countyAll .list ul li").remove();
    if (page == 1) {
        $(".countyAll .pre a").removeClass("can");
    } else {
        $(".countyAll .pre a").addClass("can");
    }
    var start;
    var end;
    if (page <= 1) {
        page = 1;
        $(".countyAll .pre a").removeClass("can");
        $(".countyAll .next a").addClass("can");
    }
    if (countyTotalPageAll == 1) {
        $(".countyAll .next a").removeClass("can");
        $(".countyAll .pre a").removeClass("can");
    }
    if (page >= countyTotalPageAll) {
        page = countyTotalPageAll;
        $(".countyAll .next a").removeClass("can");
        start = (page - 1) * pa_pageSize;
        end = countiesAll.length;
    } else if (page == 1) {
        start = (page - 1) * pa_pageSize;
        end = start + pa_pageSize;
        $(".countyAll .pre a").removeClass("can");
        $(".countyAll .next a").addClass("can");
    } else {
        start = (page - 1) * pa_pageSize;
        end = start + pa_pageSize;
        $(".countyAll .next a").addClass("can");
        $(".countyAll .pre a").addClass("can");
    }
    for (var i = start; i < end; i++) {
        var c_id = countiesAll[i].id;
        var countyName = countiesAll[i].areaName.substr(0, 4);;
        var li = $('<li><a href="javascript:onclick=addrInputAll(' + i + ')" id="' + c_id + '">' + countyName + '</a></li>');
        $(".countyAll .list ul").append(li);
    }
    $(".countyAll .list #countyPage1").remove();
    $(".countyAll .list").append("<label id='countyPage1' style='display:none;'>" + page + "</label>");
}

function addrInputAll(i) {
    var countyId = $.trim(countiesAll[i].id);
    $(".con .hotdepartmentAll .list a input").removeClass("current");
    $(".con .hotdepartmentAll .list a input[id='" + departmentIdAll + "']").addClass("current");
    $(".con .countyAll .list a").removeClass("current");
    $(".con .countyAll .list a[id='" + countyId + "']").addClass("current");
    allProId = $("body").data("pAllId");
    departmentIdAll = $("body").data("cAllId");
    var p = null;
    $.each(alldepartments, function(i, department) {
            if (department.id == allProId) {
                p = department.departmentName;
                return false;
            }
        });
    var c = null;
    $.each(alldepartments, function(i, department) {
            if (department.id == departmentIdAll) {
                c = department.name;
                return false;
            }
        });
    var a = null;
    $.each(countiesAll, function(i, county) {
            if (county.id == countyId) {
                a = county.areaName;
                return false;
            }
        });
    var nameValue = $("input.current2");
    nameValue.removeClass("iGrays");
    $(".departmentdepartmentAll").hide();
    var rtn = p + "-" + c + "-" + a;
    $("input.current2").val(rtn);
    $("input.current2").focus();
    $(".backifname").hide();
    var nameValue = $("input.current2").attr("name");
    if (nameValue == "consignor.addrProdepartment") {
        $("#departmentId").val(allProId);
        $("#departmentId").val(departmentIdAll);
    }
    if (nameValue == "order.caddrProdepartment")
    {
        $("input[name='order.caddrProdepartment']").trigger("change");
    }
    if (nameValue == "consigneeInfo.addrProdepartment")
    {
        $("input[name='consigneeInfo.addrProdepartment']").trigger("change");
    }
    if (nameValue == 'template.caddrProdepartment')
    {
        $("input[name='template.caddrProdepartment']").trigger("change");
    }
}

function hotdepartmentAddrInputAll(prodepartmentId) {
    allProId = prodepartmentId.split(",")[0];
    departmentIdAll = prodepartmentId.split(",")[1];
    var departmentCurName = prodepartmentId.split(",")[2];
    $("body").data("nameOfdepartmentAll", departmentCurName);
    $("body").data("pAllId", allProId);
    $("body").data("cAllId", departmentIdAll);
    $.each(alldepartments,
        function(i, pro) {
            if (pro.id == allProId) {
                $("body").data("pAllName", pro.departmentName);
            }
        });
    countiesAll = [];
    var j = 0;
    $.each(allAreas,
        function(i, county) {
            if (county.departmentId == departmentIdAll) {
                countiesAll[j++] = county;
            }
        });
    countyTotalPageAll = Math.ceil(countiesAll.length / pa_pageSize);
    $(".departmentdepartmentAll").find(".tabs").find("a").removeClass("current");
    $(".departmentdepartmentAll .tabs").find("#countyAll").addClass("current");
    $(".con .departmentAll .list a").removeClass("current");
    $(".con .departmentAll .list a[id='" + departmentIdAll + "']").addClass("current");
    $(".departmentdepartmentAll").find(".con").children().hide();
    $(".departmentdepartmentAll").find(".con").find(".countyAll").show();
    $(".con .departmentAll .list a").removeClass("current");
    allCountyPage(1);
}
