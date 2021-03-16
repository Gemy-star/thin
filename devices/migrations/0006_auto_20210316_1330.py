# Generated by Django 3.1.7 on 2021-03-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20210307_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thindevicesunits',
            name='name',
            field=models.CharField(blank=True, choices=[('إدارة المشاة', 'إدارة المشاة'), ('إدارة المدرعات', 'إدارة المدرعات'), ('إدارة المدفعية', 'إدارة المدفعية'), ('إدارة المركبات', 'إدارة المركبات'), ('إدارة الشرطة العسكرية', 'إدارة الشرطة العسكرية'), ('إدارة الشؤون المعنوية', 'إدارة الشؤون المعنوية'), ('جهاز الرياضة العسكري', 'جهاز الرياضة العسكري'), ('هيئة التدريب للقوات المسلحة', 'هيئة التدريب للقوات المسلحة'), ('هيئة التفتيش للقوات المسلحة', 'هيئة التفتيش للقوات المسلحة'), ('إدارة الأسلحة والذخيرة', 'إدارة الأسلحة والذخيرة'), ('إدارة البحوث الفنية والتطوير', 'إدارة البحوث الفنية والتطوير'), ('مركز التنمية البشرية والعلوم السلوكية', 'مركز التنمية البشرية والعلوم السلوكية'), ('إدارة نوادي وفاندق ضباط ق.م', 'إدارة نوادي وفاندق ضباط ق.م'), (' جهاز مشروعات الخدمة الوطنية', 'جهاز مشروعات الخدمة الوطنية'), ('هيئة القضاء العسكري', 'هيئة القضاء العسكري'), ('إدارة المدعي العام', 'إدارة المدعي العام'), ('إدارة المحاكم العسكرية', 'إدارة المحاكم العسكرية'), ('إدارة الحرب الكيمائية', 'إدارة الحرب الكيمائية'), ('إدارة المتاحف العسكرية', 'إدارة المتاحف العسكرية'), ('قيادة قوات حرس الحدود', 'قيادة قوات حرس الحدود'), ('قيادة قوات الدفاع الشعبي والعسكري', 'قيادة قوات الدفاع الشعبي والعسكري'), ('إدارة الموسيقات العسكرية', 'إدارة الموسيقات العسكرية'), ('دار المحفوظات المركزية', 'دار المحفوظات المركزية'), ('المركز الرئيسية للتنبؤات الجوية', 'المركز الرئيسية للتنبؤات الجوية'), ('جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م', 'جهاز مراقبة وضمان الجودة/هيئة التسليح ق.م'), (' إدارة التعليم والتدريب المهني', 'إدارة التعليم والتدريب المهني'), ('قيادة القوات الجوية', 'قيادة القوات الجوية'), ('المركز الإعلامي العسكري', 'المركز الإعلامي العسكري'), ('مركز تطوير وصيانة معدات النظم الألية', 'مركز تطوير وصيانة معدات النظم الألية'), ('مركز تدريب الية القيادة والسيطرة', 'مركز تدريب الية القيادة والسيطرة'), ('المنظومة تحرير', 'المنظومة تحرير'), ('إدارة المحفوظات المركزية', 'إدارة المحفوظات المركزية'), ('إدارة المياه', 'إدارة المياه'), ('إدارة الإشارة', 'إدارة الإشارة'), ('CCTV ', 'CCTV'), ('دفاع جوي', 'دفاع جوي'), ('جهاز تنمية الموارد المالية', 'جهاز تنمية الموارد المالية'), ('مؤسسة صندوق الجلاء للقوات المسلحة', 'مؤسسة صندوق الجلاء للقوات المسلحة'), ('صندوق التأميني التكميلي', 'صندوق التأميني التكميلي'), ('مؤسسة القروض', 'مؤسسة القروض'), ('صندوق التأمين الخاص', 'صندوق التأمين الخاص'), ('صندوق إسكان أفراد القوات المسلحة', 'صندوق إسكان أفراد القوات المسلحة'), ('هيئة الشؤون المالية للقوات المسلحة', 'هيئة الشؤون المالية للقوات المسلحة'), ('إدارة التفتيش والمحاسبات', 'إدارة التفتيش والمحاسبات'), ('إدارة الميزانية', 'إدارة الميزانية'), ('إدارة العلاقات العامة والتمويل الخارجي', 'إدارة العلاقات العامة والتمويل الخارجي'), ('الإدارة المركزية للمحاسبات', 'الإدارة المركزية للمحاسبات'), ('إدارة التأمين والمعاشات', 'إدارة التأمين والمعاشات'), ('هيئة التنظيم والإدارة للقوات المسلحة', 'هيئة التنظيم والإدارة للقوات المسلحة'), ('إدارة التجنيد والتعبئة', 'إدارة التجنيد والتعبئة'), ('إدارة السجلات العسكرية', 'إدارة السجلات العسكرية'), ('فرع الإنتقاء والتوجيه', 'فرع الإنتقاء والتوجي'), ('إدارة شؤون العاملين المدنيين', 'إدارة شؤون العاملين المدنيين')], max_length=255, null=True),
        ),
    ]
