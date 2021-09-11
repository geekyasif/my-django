from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, PostComment
from django.contrib import messages
# from blog.templatestags import get_dict
from blog.templatetags import get_dict


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = { 'allPosts' : allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    comments = PostComment.objects.filter(post=post, parent=None)
    replies = PostComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)   
    context = {'post' : post, 'comments' : comments, 'replyDict': replyDict}
    return render(request, 'blog/blogPost.html', context)


def Comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        PostSno = request.POST.get('PostSno')
        post = Post.objects.get(sno=PostSno)
        parentSno = request.POST.get('parentSno')

        if parentSno == "":
            comment = PostComment(comment = comment, user = user, post = post)
            comment.save()
            messages.success(request, "Your comment has been submitted successfully")
        else:
            parent = PostComment.objects.get(sno=parentSno)
            comment = PostComment(comment = comment, user = user, post = post, parent = parent)
            comment.save()
            messages.success(request, "Your reply has been submitted successfully")

    return redirect(f"/blog/{post.slug}")