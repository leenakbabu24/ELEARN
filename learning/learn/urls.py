from django.urls import path
import learn.views

urlpatterns = [
    path('',learn.views.home,name='home'),
    path('home',learn.views.home,name='home'),
    path('news',learn.views.news,name='news'),
    path('about',learn.views.about,name='about'),
    path('add_blog',learn.views.add_blog,name='add_blog'),
    path('view_blog', learn.views.view_blog, name='view_blog'),
    path('contact',learn.views.contact,name='contact'),
    path('courses',learn.views.courses,name='courses'),
    path('login/',learn.views.login,name='login'),
    path('student_register',learn.views.student_register,name='student_register'),
    path('register_tr',learn.views.register_tr,name='register_tr'),
    path('admin_rg',learn.views.admin_rg,name='admin_rg'),
    path('admin_home',learn.views.admin_home,name='admin_home'),
    path('student_home', learn.views.student_home, name='student_home'),
    path('teacher_home', learn.views.teacher_home, name='teacher_home'),
    path('logout', learn.views.logout, name='logout'),
    path('abb', learn.views.abb, name='abb'),
    path('about_content',learn.views.about_content,name='about_content'),
    path('blogs_admin', learn.views.blogs_admin, name='blogs_admin'),
    path('blog_approves/<id>', learn.views.blog_approves, name='blog_approves'),
    path('blog_rejects/<id>', learn.views.blog_rejects, name='blog_rejects'),
    path('blog_delete/<id>', learn.views.blog_delete, name='blog_delete'),
    path('g_m', learn.views.g_m, name='g_m'),
    path('guest_message', learn.views.guest_message, name='guest_message'),
    path('delete_g_msg/<id>', learn.views.delete_g_msg, name='delete_g_msg'),
    path('update_pr_tr', learn.views.update_pr_tr, name='update_pr_tr'),
    path('update_pr_st', learn.views.update_pr_st, name='update_pr_st'),
    path('adm_prof', learn.views.adm_prof, name='adm_prof'),
    path('del_admin/<id>', learn.views.del_admin, name='del_admin'),
    path('edit_admin', learn.views.edit_admin, name='edit_admin'),
    path('update_admin', learn.views.update_admin, name='update_admin'),
    path('bnb', learn.views.bnb, name='bnb'),
    path('sub_tr', learn.views.sub_tr, name='sub_tr'),
    path('edit_subject/<id>/<idd>/<idm>', learn.views.edit_subject, name='edit_subject'),
    path('delete_subject/<id>/<idd>/<idm>', learn.views.delete_subject, name='delete_subject'),
    path('add_subject', learn.views.add_subject, name='add_subject'),
    path('chap_tr', learn.views.chap_tr, name='chap_tr'),
    path('edit_chapter/<id>/<idd>/<idk>/<idm>', learn.views.edit_chapter, name='edit_chapter'),
    path('delete_chapter/<id>/<idd>/<idk>/<idm>', learn.views.delete_chapter, name='delete_chapter'),
    path('add_chapter', learn.views.add_chapter, name='add_chapter'),
    path('add_chapter1', learn.views.add_chapter1, name='add_chapter1'),
    path('ch_co_tr', learn.views.ch_co_tr, name='ch_co_tr'),
    path('cont_tr', learn.views.cont_tr, name='cont_tr'),
    path('edit_content/<id>', learn.views.edit_content, name='edit_content'),
    path('delete_content/<id>', learn.views.delete_content, name='delete_content'),
    path('add_ch_con', learn.views.add_ch_con, name='add_ch_con'),
    path('add_chapter_content', learn.views.add_chapter_content, name='add_chapter_content'),
    path('add_chapter_c0', learn.views.add_chapter_c0, name='add_chapter_c0'),
    path('add_chapter_c1', learn.views.add_chapter_c1, name='add_chapter_c1'),
    path('add_chapter_c2', learn.views.add_chapter_c2, name='add_chapter_c2'),
    path('paid', learn.views.paid, name='paid'),
    path('stu_buk_teacher', learn.views.stu_buk_teacher, name='stu_buk_teacher'),
    path('stu_buk_teacherr/<id>', learn.views.stu_buk_teacherr, name='stu_buk_teacherr'),
    path('st_sub_selnew', learn.views.st_sub_selnew, name='st_sub_selnew'),
    path('stu_sub_selnew', learn.views.stu_sub_selnew, name='stu_sub_selnew'),
    path('st_sub_selnew2', learn.views.st_sub_selnew2, name='st_sub_selnew2'),
    path('st_sub_selnew1', learn.views.st_sub_selnew1, name='st_sub_selnew1'),
    path('disp_teach', learn.views.disp_teach, name='disp_teach'),
    path('stu_buk_acc', learn.views.stu_buk_acc, name='stu_buk_acc'),
    path('stu_accept/<id>', learn.views.stu_accept, name='stu_accept'),
    path('stu_reject/<id>', learn.views.stu_reject, name='stu_reject'),
    path('stu_delete/<id>', learn.views.stu_delete, name='stu_delete'),
    path('notiffy', learn.views.notiffy, name='notiffy'),
    path('st_book_courses', learn.views.st_book_courses, name='st_book_courses'),
    path('acc_chapter1', learn.views.acc_chapter1, name='acc_chapter1'),
    path('acc_chapter2', learn.views.acc_chapter2, name='acc_chapter2'),
    path('acc_chapter/<id>/<ikm>/<sub>', learn.views.acc_chapter, name='acc_chapter'),
    path('compp', learn.views.compp, name='compp'),
    path('st_progress', learn.views.st_progress, name='st_progress'),
    path('sched_test', learn.views.sched_test, name='sched_test'),
    path('sched_test1', learn.views.sched_test1, name='sched_test1'),
    path('sched_test2', learn.views.sched_test2, name='sched_test2'),
    path('sched_test3', learn.views.sched_test3, name='sched_test3'),
    path('ex_not', learn.views.ex_not, name='ex_not'),
    path('start_test', learn.views.start_test, name='start_test'),
    path('save_exam', learn.views.save_exam, name='save_exam'),
    path('exam_result', learn.views.exam_result, name='exam_result'),
    path('exam_result1', learn.views.exam_result1, name='exam_result1'),
    path('delete_ex_re/<id>', learn.views.delete_ex_re, name='delete_ex_re'),
    path('delete_test', learn.views.delete_test, name='delete_test'),
    path('delete_test1/<id>', learn.views.delete_test1, name='delete_test1'),
    path('upl_cer', learn.views.upl_cer, name='upl_cer'),
    path('upload_cert', learn.views.upload_cert, name='upload_cert'),
    path('do_cer', learn.views.do_cer, name='do_cer'),
    path('del_cert', learn.views.del_cert, name='del_cert'),
    path('delete_cert/<id>', learn.views.delete_cert, name='delete_cert'),
    path('block', learn.views.block, name='block'),
    path('blocks/<id>', learn.views.blocks, name='blocks'),
    path('blocks1/<id>', learn.views.blocks1, name='blocks1'),
    path('allows/<id>', learn.views.allows, name='allows'),
    path('allows1/<id>', learn.views.allows1, name='allows1'),
    path('feedback', learn.views.feedback, name='feedback'),
    path('feedbak', learn.views.feedbak, name='feedbak'),
    path('delete_feedback/<id>', learn.views.delete_feedback, name='delete_feedback'),
    path('message2', learn.views.message2, name='message2'),
    path('reply_msg_student/<id>', learn.views.reply_msg_student, name='reply_msg_student'),
    path('sent_msg_student', learn.views.sent_msg_student, name='sent_msg_student'),
    path('del_msg_student/<id>', learn.views.del_msg_student, name='del_msg_student'),
    path('m_m2',learn.views.m_m2,name='m_m2'),
    path('message', learn.views.message, name='message'),
    path('reply_msg_admin/<id>', learn.views.reply_msg_admin, name='reply_msg_admin'),
    path('del_msg_admin/<id>', learn.views.del_msg_admin, name='del_msg_admin'),
    path('sent_msg_admin', learn.views.sent_msg_admin, name='sent_msg_admin'),
    path('m_m', learn.views.m_m, name='m_m'),
    path('message1', learn.views.message1, name='message1'),
    path('reply_msg_teacher/<id>', learn.views.reply_msg_teacher, name='reply_msg_teacher'),
    path('del_msg_teacher/<id>', learn.views.del_msg_teacher, name='del_msg_teacher'),
    path('sent_msg_teacher', learn.views.sent_msg_teacher, name='sent_msg_teacher'),
    path('m_m1', learn.views.m_m1, name='m_m1'),
    path('sub_ad', learn.views.sub_ad, name='sub_ad'),
    path('subject_ad', learn.views.subject_ad, name='subject_ad'),
    path('edit_subject1/<id>/<idd>/<idt>/<pkm>', learn.views.edit_subject1, name='edit_subject1'),
    path('delete_subject1/<id>/<idd>/<idt>/<pkm>', learn.views.delete_subject1, name='delete_subject1'),
    path('chap_ad', learn.views.chap_ad, name='chap_ad'),
    path('chapter_ad', learn.views.chapter_ad, name='chapter_ad'),
    path('edit_chapter1/<id>/<idd>/<idt>/<idk>/<pkm>', learn.views.edit_chapter1, name='edit_chapter1'),
    path('delete_chapter1/<id>/<idd>/<idt>/<idk>/<pkm>', learn.views.delete_chapter1, name='delete_chapter1'),
    path('chap_content', learn.views.chap_content, name='chap_content'),
    path('edit_content1/<id>', learn.views.edit_content1, name='edit_content1'),
    path('delete_content1/<id>', learn.views.delete_content1, name='delete_content1'),
    path('atten', learn.views.atten, name='atten'),
    path('reg_msg', learn.views.reg_msg, name='reg_msg'),
]