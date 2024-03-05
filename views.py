from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Elibrary,EMember,ERecord
from django.contrib.auth.models import User
from datetime import datetime
from django.db import transaction
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email_id')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Passwords do not match, Try again.")
        else:
            myUser = User.objects.create_user(uname,email,pass1)
            myUser.save()
            return redirect('login')
    return render(request,'signup.html')

def LogIn(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pass1 = request.POST.get("password")
        user = authenticate(request, username = uname, password = pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Entering username and password is necessary..')


    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def AddBooks(request):
    return render(request,'AddBooks.html')

@login_required(login_url='login')
def Display(request):
    if request.method == 'GET':
        id = request.GET['id']
        Name = request.GET['Name']
        Subject = request.GET['Subject']
        Description = request.GET['Description']
        Semester = int(request.GET['Semester'])
        Quantity = int(request.GET['Quantity'])
        Price = int(request.GET['Price'])

        # Creating a new instance of the Library model
        users = Elibrary(id=id,Name=Name, Subject=Subject, Description=Description, Semester=Semester, Quantity=Quantity, Price=Price)
        users.save()
        # print(Name,Subject,Description,Semester,Quantity,Price)
        # users = library(Name=Name, Subject=Subject, Description=Description, Semester=Semester, Quantity=Quantity, Price=Price)

        # users.save()
        result = Elibrary.objects.all().values()
        return render(request, "Display.html",{'result':result})
    
@login_required(login_url='login')
def Delete(request):
    # object = request.GET['id']
    # Elibrary.objects.filter(id = object).delete()
    # result = Elibrary.objects.all()
    # return render(request,'Display.html',{'result':result})

    if 'id' in request.GET:
        object_id = request.GET['id']
        Elibrary.objects.filter(id=object_id).delete()
    result = Elibrary.objects.all()
    return render(request, 'Display.html', {'result': result})

@login_required(login_url='login')
def DisplayBtn(request):        
    result = Elibrary.objects.all().values()
    return render(request, "Display.html",{'result':result})

@login_required(login_url='login')
def UpdateBooks(request):
    object_id = request.GET['id']
    print(object_id)
    data= Elibrary.objects.values().filter(id=object_id)
    for value in data:
        Id = value['id']
        name = value['Name']
        subject = value['Subject']
        description = value['Description']
        sem = value['Semester']
        quantity = value['Quantity']
        price = value['Price']
    return render(request,'update.html',{'Id':Id,'name':name,'subject':subject,'description':description,'sem':sem,'quantity':quantity,'price':price})

@login_required(login_url='login')
def UpdatedBooks(request):
    if request.method == 'GET':
        id = request.GET['id']
        name = request.GET['Name']
        subject = request.GET['Subject']
        description = request.GET['Description']
        semester = request.GET['Semester']
        quantity = request.GET['Quantity']
        price = request.GET['Price']
        # Creating a new instance of the Library model
        users = Elibrary.objects.filter(id=id).update(Name=name, Subject=subject, Description=description, Semester=semester, Quantity=quantity, Price=price)
        
        # users.save()
        # print(Name,Subject,Description,Semester,Quantity,Price)
        # users = Elibrary(Name=Name, Subject=Subject, Description=Description, Semester=Semester, Quantity=Quantity, Price=Price)

        # users.save()

        result = Elibrary.objects.all().values()
        return render(request, "Display.html",{'result':result})
    
@login_required(login_url='login')
def Members(request):
    return render(request,'AddMembers.html')

@login_required(login_url='login')
def AddMembers(request):
    id = request.GET['id']
    name = request.GET['Name']
    sem = request.GET['Semester']
    branch = request.GET['Branch']
    mob_no = request.GET['Mob_No']

    users = EMember(id = id,Name = name,Semester = sem,Branch = branch,Mob_No = mob_no)
    users.save()
    data = EMember.objects.all().values()
    
    return render(request,'DispMembers.html',{'data':data})

@login_required(login_url='login')
def DispMembers(request):
    data = EMember.objects.all().values()
    return render(request, "DispMembers.html",{'data':data})

@login_required(login_url='login')
def Deleted(request):
    if 'id' in request.GET:
        object_id = request.GET['id']
        EMember.objects.filter(id=object_id).delete()
    data = EMember.objects.all()
    return render(request, 'DispMembers.html', {'data': data})

@login_required(login_url='login')
def UpdateMembers(request):
    object_id = request.GET['id']
    print(object_id)
    data= EMember.objects.values().filter(id=object_id)
    Id = name = semester = branch = mob_no = None
    for value in data:
        Id = value['id']
        name = value['Name']
        semester = value['Semester']
        branch = value['Branch']
        mob_no = value['Mob_No']
    return render(request,'UpdateMembers.html',{'Id':Id,
                                'name':name,'semester':semester,
                                'branch':branch,'mob_no':mob_no})

@login_required(login_url='login')
def UpdatedMembers(request):
    if request.method == 'GET':
        id = request.GET['id']
        name = request.GET['Name']
        semester = request.GET['Semester']
        branch = request.GET['Branch']
        mob_no = request.GET['Mob_No']
        users = EMember.objects.filter(id=id).update(Name=name, Semester=semester,
                                                     Branch=branch, Mob_No=mob_no)

        data = EMember.objects.all().values()
        return render(request, "DispMembers.html",{'data':data})
    
@login_required(login_url='login')
def Issue(request):
    return render(request, 'Issue.html')

# def Issued(request):
#     if request.method == 'GET':
#         book_id = request.GET['Book_id']
#         member_id = request.GET['Member_id']
#         issue_date = request.GET['issue_date']
#         return_date = request.GET['Return_date']
#         status = request.GET.get('Status',True)
#         status = status == 'on'
        
#         book_instance = Elibrary.objects.get(id = book_id)
#         member_instance = EMember.objects.get(id = member_id)

#         record_instance = ERecord.objects.create(Book_id=book_instance,
#             Member_id=member_instance,
#             issue_date=issue_date,
#             Return_date=return_date,
#             Status=status)
#         book_instance.Quantity -= 1
#         # record_instance = ERecord(id,book_instance,member_instance,issue_date,return_date,status)

#         book_instance.save()

#         data = ERecord.objects.all().values()
#         return render(request,'Issued.html',{'data':data})

@login_required(login_url='login')
def Issued(request):
    if request.method == 'GET':
        id = request.GET['id']
        book_id = request.GET['Book_id']
        member_id = request.GET['Member_id']
        issue_date = request.GET['issue_date']
        return_date = request.GET['Return_date']
        status = request.GET.get('Status', True)
        status = status == 'on'

        try:
            book_instance = Elibrary.objects.get(id=book_id)
            if book_instance.Quantity <= 0:
                return HttpResponse("No books available for issuance.")

            member_instance = EMember.objects.get(id=member_id)
            book_name = book_instance.Name
            member_name = member_instance.Name
            print(book_name)
            print('5464jbhdj ')

            record_instance = ERecord.objects.create(id = id,Book_id=book_instance,
                                                      Member_id=member_instance,
                                                      issue_date=issue_date,
                                                      Return_date=return_date,
                                                      Status=status)
            book_instance.Quantity -= 1
            book_instance.save()

            data = ERecord.objects.all().select_related('Book_id','Member_id').values(
        'id', 'Book_id_id', 'Book_id__Name', 'Member_id_id','Member_id__Name', 'issue_date', 'Return_date', 'Status'
            )
            return render(request, "Issued.html", {'data': data})
        except Elibrary.DoesNotExist:
            return HttpResponse("Book not found.")
        except EMember.DoesNotExist:
            return HttpResponse("Member not found.")

    return HttpResponse("Invalid request method.")

@login_required(login_url='login')
def DispIssue(request):
    data = ERecord.objects.all().select_related('Book_id','Member_id').values(
        'id', 'Book_id_id', 'Book_id__Name', 'Member_id_id','Member_id__Name', 'issue_date', 'Return_date', 'Status'
    )
    return render(request, "Issued.html", {'data': data})

@login_required(login_url='login')
def UpdateIssue(request):
    object_id = request.GET.get('id')
    print(object_id)

    try:
        record = ERecord.objects.get(id=object_id)
        book_id = record.Book_id
        member_id = record.Member_id
        issue_date = record.issue_date
        return_date = record.Return_date
        status = record.Status 

        return render(request, 'UpdateIssue.html', {
            'Id': object_id,
            'book_id':book_id,
            'member_id':member_id,
            'issue_date': issue_date,
            'return_date': return_date,
            'status': status
        })
    except ERecord.DoesNotExist:
        return HttpResponse("Record does not exist")

@login_required(login_url='login')
def UpdatedIssue(request):
    if request.method == 'GET':
        id = request.GET['id']
        book_id = request.GET['Book_id']
        member_id = request.GET['Member_id']
        issue_date = request.GET['issue_date']
        return_date = request.GET['Return_date']
        status = request.GET.get('Status',True)
        status = status == 'on'

        object_id = request.GET.get('id')
        record = ERecord.objects.get(id=object_id)

        with transaction.atomic():
            users = ERecord.objects.filter(id=id).update(
                Book_id = book_id,
                Member_id = member_id,
                issue_date=issue_date,
                Return_date=return_date,
                Status=status
            )

            if not status:
                record.Book_id.Quantity += 1
                record.Book_id.save()

        data = ERecord.objects.all().select_related('Book_id','Member_id').values(
        'id', 'Book_id_id', 'Book_id__Name', 'Member_id_id','Member_id__Name', 
        'issue_date', 'Return_date', 'Status'
            )
        return render(request, "Issued.html", {'data': data})



# # def Issued(request):
# #     if request.method == 'GET':
# #         id = request.GET['id']
# #         book_id = request.GET['Book_id']
# #         member_id = request.GET['Member_id']
# #         issue_date = request.GET['Issue_date']
# #         return_date = request.GET['Return_date']
# #         status = request.GET.get('Status',True)

# #         # issue_date = datetime.strptime(issue_date,'%Y-%m-%d').date()
# #         # return_date = datetime.strptime(return_date,'%Y-%m-%d').date()

# #         status = status == 'on'

# #         book_instance = get_object_or_404(Elibrary,id = book_id)
# #         member_instance = get_object_or_404(EMember,id = member_id)

# #         # record_instance = ERecord(id,book_instance,member_instance,issue_date,return_date,status)

# #         record_instance = ERecord(id = id,Book_id = book_instance,
# #                          Member_id = member_instance, Issue_date = issue_date,
# #                          Return_date = return_date,Status = status)

# #         record_instance.save()
# #         data = ERecord.objects.all().values()
# #         return render(request,'Issued.html',{'data':data})
