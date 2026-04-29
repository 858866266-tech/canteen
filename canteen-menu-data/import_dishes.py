#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成历史菜品库 JSON"""
import json

# 完整去重菜谱，按分类整理
ALL = [
    # 汤类 (soup)
    ("鸡汤", "soup", ["lunch","dinner"]),
    ("鸡汤（板栗）", "soup", ["lunch","dinner"]),
    ("鸡汤（五花腩，药材）", "soup", ["lunch","dinner"]),
    ("鸡汤（五花腩，板栗）", "soup", ["lunch","dinner"]),
    ("鸡汤（五花腩，核桃）", "soup", ["lunch","dinner"]),
    ("鸡汤放深薯", "soup", ["lunch","dinner"]),
    ("鸡汤放黄花菜", "soup", ["lunch","dinner"]),
    ("椰子鸡汤", "soup", ["lunch","dinner"]),
    ("鸡项椰子汤", "soup", ["lunch","dinner"]),
    ("鸡项猪肚汤", "soup", ["lunch","dinner"]),
    ("鸡项药材汤", "soup", ["lunch","dinner"]),
    ("竹丝鸡熟地汤", "soup", ["lunch","dinner"]),
    ("胡椒猪肚鸡汤", "soup", ["lunch","dinner"]),
    ("猪肚鸡汤", "soup", ["lunch","dinner"]),
    ("阉鸡（五花腩）药材汤", "soup", ["lunch","dinner"]),
    ("阉鸡（药材）", "soup", ["lunch","dinner"]),
    ("阉鸡（板栗）", "soup", ["lunch","dinner"]),
    ("鸽子瘦肉汤", "soup", ["lunch","dinner"]),
    ("鸽子瘦肉药材汤", "soup", ["lunch","dinner"]),
    ("白鸽瘦肉汤", "soup", ["lunch","dinner"]),
    ("骨头莲藕汤", "soup", ["lunch","dinner"]),
    ("骨头祛湿汤", "soup", ["lunch","dinner"]),
    ("骨头深薯汤", "soup", ["lunch","dinner"]),
    ("骨头药材汤", "soup", ["lunch","dinner"]),
    ("骨头土茯苓薏米汤", "soup", ["lunch","dinner"]),
    ("骨头黑豆汤", "soup", ["lunch","dinner"]),
    ("骨头巴戟杜仲汤", "soup", ["lunch","dinner"]),
    ("骨头牛大力黑豆汤", "soup", ["lunch","dinner"]),
    ("扇骨药材汤", "soup", ["lunch","dinner"]),
    ("雄鱼头汤", "soup", ["lunch","dinner"]),
    ("雄鱼头汤（川穹白芷）", "soup", ["lunch","dinner"]),
    ("猪手醋汤", "soup", ["lunch","dinner"]),
    ("羊肉汤", "soup", ["lunch","dinner"]),
    ("牛肉当归汤", "soup", ["lunch","dinner"]),
    ("猪肉猪杂枸杞叶汤", "soup", ["lunch","dinner"]),
    ("骨底瘦肉猪杂枸杞叶汤", "soup", ["lunch","dinner"]),
    ("骨底瘦肉猪杂冬瓜汤", "soup", ["lunch","dinner"]),
    ("紫菜蛋花汤", "soup", ["lunch","dinner"]),
    ("紫菜鸡蛋汤", "soup", ["lunch","dinner"]),
    ("鸡蛋丝瓜汤", "soup", ["lunch","dinner"]),
    ("鸡蛋裙带菜汤", "soup", ["lunch","dinner"]),
    ("鸡蛋麦菜汤", "soup", ["lunch","dinner"]),
    ("鸡蛋紫菜汤", "soup", ["lunch","dinner"]),
    ("瑶柱蚝士瘦肉粥", "staple", ["breakfast","lunch","dinner"]),
    ("虾粥", "staple", ["breakfast","lunch","dinner"]),
    ("鲜虾瘦肉粥", "staple", ["breakfast","lunch","dinner"]),
    ("瘦肉猪杂粥", "staple", ["breakfast","lunch","dinner"]),
    ("牛肉粥", "staple", ["breakfast","lunch","dinner"]),
    ("白粥", "staple", ["breakfast","lunch","dinner"]),
    ("花生黄豆鸡脚", "soup", ["lunch","dinner"]),

    # 荤菜 - 家禽
    ("沙姜蒜子炒鸡", "meat", ["lunch","dinner"]),
    ("沙姜蒜子生蒜炒鸡", "meat", ["lunch","dinner"]),
    ("沙姜蒜子葱炒鸡", "meat", ["lunch","dinner"]),
    ("沙姜鸡爪", "meat", ["lunch","dinner"]),
    ("盐焗鸡", "meat", ["lunch","dinner"]),
    ("盐摸鸡", "meat", ["lunch","dinner"]),
    ("沙姜焗猪手", "meat", ["lunch","dinner"]),
    ("焗鸡脚", "meat", ["lunch","dinner"]),
    ("焗猪手", "meat", ["lunch","dinner"]),
    ("炸鸡中翅", "meat", ["lunch","dinner"]),
    ("生蒜炒鸡", "meat", ["lunch","dinner"]),
    ("炒年例鸡", "meat", ["lunch","dinner"]),
    ("白切鸡", "meat", ["lunch","dinner"]),

    # 荤菜 - 猪肉
    ("腐竹炒肉", "meat", ["lunch","dinner"]),
    ("豆角炒肉", "meat", ["lunch","dinner"]),
    ("丝瓜炒肉", "meat", ["lunch","dinner"]),
    ("荷兰豆炒腊肠", "meat", ["lunch","dinner"]),
    ("土豆炒肉", "meat", ["lunch","dinner"]),
    ("口蘑炒肉", "meat", ["lunch","dinner"]),
    ("平菇炒肉", "meat", ["lunch","dinner"]),
    ("竹笋炒肉", "meat", ["lunch","dinner"]),
    ("茄子炒肉", "meat", ["lunch","dinner"]),
    ("蒸排骨", "meat", ["lunch","dinner"]),
    ("香菇肉饼", "meat", ["lunch","dinner"]),
    ("马蹄肉饼", "meat", ["lunch","dinner"]),
    ("焖鲩鱼腩", "meat", ["lunch","dinner"]),
    ("蒸鲩鱼腩", "meat", ["lunch","dinner"]),
    ("煎鲩鱼腩", "meat", ["lunch","dinner"]),
    ("腐竹焖鲩鱼腩", "meat", ["lunch","dinner"]),
    ("鲩鱼腩焖腐竹", "meat", ["lunch","dinner"]),
    ("猪手醋", "meat", ["lunch","dinner"]),
    ("香芹炒脆肉鲩鱼", "meat", ["lunch","dinner"]),
    ("紫苏炒脆肉鲩鱼", "meat", ["lunch","dinner"]),
    ("青椒炒猪耳朵", "meat", ["lunch","dinner"]),
    ("尖椒炒猪耳朵", "meat", ["lunch","dinner"]),
    ("青瓜炒罗定鱼腐", "meat", ["lunch","dinner"]),
    ("罗定鱼腐", "meat", ["lunch","dinner"]),
    ("咖喱土豆牛肉", "meat", ["lunch","dinner"]),
    ("菜干蒸肉饼", "meat", ["lunch","dinner"]),
    ("豆炸焖腩肉", "meat", ["lunch","dinner"]),
    ("豆炸酿", "meat", ["lunch","dinner"]),
    ("土豆炒牛肉", "meat", ["lunch","dinner"]),

    # 荤菜 - 牛肉
    ("萝卜炖牛腩", "meat", ["lunch","dinner"]),
    ("白萝卜炖牛腩", "meat", ["lunch","dinner"]),
    ("白萝卜丝炒牛肉", "meat", ["lunch","dinner"]),
    ("牛肉炒芥兰", "meat", ["lunch","dinner"]),
    ("牛肉炒白萝卜", "meat", ["lunch","dinner"]),
    ("藕带炒牛肉", "meat", ["lunch","dinner"]),
    ("葱姜炒牛百叶", "meat", ["lunch","dinner"]),

    # 荤菜 - 鱼
    ("蒸鲈鱼", "meat", ["lunch","dinner"]),
    ("煎鲈鱼", "meat", ["lunch","dinner"]),
    ("蒸罗非", "meat", ["lunch","dinner"]),
    ("煎罗非", "meat", ["lunch","dinner"]),
    ("蒸小罗非", "meat", ["lunch","dinner"]),
    ("煎小罗非", "meat", ["lunch","dinner"]),
    ("煎杂鱼", "meat", ["lunch","dinner"]),
    ("煎仓鱼", "meat", ["lunch","dinner"]),
    ("盐焗虾", "meat", ["lunch","dinner"]),
    ("咖喱黄金鱼蛋", "meat", ["lunch","dinner"]),
    ("黄金鱼蛋", "meat", ["lunch","dinner"]),
    ("椒盐雄鱼肉", "meat", ["lunch","dinner"]),

    # 荤菜 - 内脏/其他
    ("尖椒炒鸡肾", "meat", ["lunch","dinner"]),
    ("尖椒炒鸡爪", "meat", ["lunch","dinner"]),

    # 素菜 - 叶菜
    ("空心菜", "veg", ["lunch","dinner"]),
    ("捏水空心菜", "veg", ["lunch","dinner"]),
    ("油麦菜", "veg", ["lunch","dinner"]),
    ("捏水油麦菜", "veg", ["lunch","dinner"]),
    ("生菜", "veg", ["lunch","dinner"]),
    ("娃娃菜", "veg", ["lunch","dinner"]),
    ("香麦菜", "veg", ["lunch","dinner"]),
    ("捏水麦菜", "veg", ["lunch","dinner"]),
    ("水麦菜", "veg", ["lunch","dinner"]),
    ("皇帝菜", "veg", ["lunch","dinner"]),
    ("西洋菜", "veg", ["lunch","dinner"]),
    ("苋菜", "veg", ["lunch","dinner"]),
    ("茼蒿", "veg", ["lunch","dinner"]),
    ("菜心", "veg", ["lunch","dinner"]),
    ("小白菜", "veg", ["lunch","dinner"]),
    ("芥兰", "veg", ["lunch","dinner"]),
    ("芥菜", "veg", ["lunch","dinner"]),
    ("水东芥菜", "veg", ["lunch","dinner"]),

    # 素菜 - 瓜果根茎
    ("青瓜炒肉", "veg", ["lunch","dinner"]),
    ("青瓜滚豆腐", "veg", ["lunch","dinner"]),
    ("青瓜衮豆腐", "veg", ["lunch","dinner"]),
    ("凉拌青瓜木耳黄花菜", "veg", ["lunch","dinner"]),
    ("盐水豆腐", "veg", ["lunch","dinner"]),
    ("煎盐水豆腐", "veg", ["lunch","dinner"]),
    ("香煎盐水豆腐", "veg", ["lunch","dinner"]),
    ("红烧日本豆腐", "veg", ["lunch","dinner"]),
    ("香煎红烧日本豆腐", "veg", ["lunch","dinner"]),
    ("番茄炒蛋", "veg", ["lunch","dinner"]),
    ("尖椒火腿炒蛋", "veg", ["lunch","dinner"]),
    ("尖椒丝炒蛋", "veg", ["lunch","dinner"]),
    ("尖椒炒蛋", "veg", ["lunch","dinner"]),
    ("尖椒煎蛋", "veg", ["lunch","dinner"]),
    ("南瓜", "veg", ["lunch","dinner"]),
    ("苦瓜酿", "veg", ["lunch","dinner"]),
    ("胡萝卜玉米炒瘦肉粒", "veg", ["lunch","dinner"]),
    ("胡萝卜玉米炒肉", "veg", ["lunch","dinner"]),
    ("莴笋炒肉", "veg", ["lunch","dinner"]),
    ("土豆", "veg", ["lunch","dinner"]),
    ("冬瓜", "veg", ["lunch","dinner"]),
    ("酸辣土豆丝", "veg", ["lunch","dinner"]),

    # 素菜 - 菇菌
    ("杏鲍菇炒肉", "veg", ["lunch","dinner"]),
    ("鸡腿菇炒肉", "veg", ["lunch","dinner"]),

    # 素菜 - 豆制品
    ("腐竹木耳炒肉", "veg", ["lunch","dinner"]),
    ("豆干炒腊肉", "veg", ["lunch","dinner"]),

    # 素菜 - 蛋/其他
    ("蒸水蛋", "veg", ["lunch","dinner"]),
    ("葱花煎蛋", "veg", ["lunch","dinner"]),
    ("韭黄炒蛋", "veg", ["lunch","dinner"]),
    ("炸热狗", "veg", ["lunch","dinner"]),
    ("荷兰豆炒肉", "veg", ["lunch","dinner"]),
    ("蒜薹炒腊肠", "veg", ["lunch","dinner"]),

    # 主食
    ("云吞", "staple", ["breakfast","lunch","dinner"]),
    ("云吞（纯肉）", "staple", ["breakfast","lunch","dinner"]),
    ("云吞（香芹）", "staple", ["breakfast","lunch","dinner"]),
    ("云吞（紫菜）", "staple", ["breakfast","lunch","dinner"]),
    ("云吞（香菇）", "staple", ["breakfast","lunch","dinner"]),
    ("捞粉", "staple", ["breakfast","lunch","dinner"]),
    ("粉皮", "staple", ["breakfast","lunch","dinner"]),
    ("炒粉", "staple", ["breakfast","lunch","dinner"]),
    ("炒面条", "staple", ["breakfast","lunch","dinner"]),
    ("面条", "staple", ["breakfast","lunch","dinner"]),
    ("蒸饺", "staple", ["breakfast","lunch","dinner"]),
    ("蒸饺（国薯馅）", "staple", ["breakfast","lunch","dinner"]),
    ("油条", "staple", ["breakfast"]),
    ("包子", "staple", ["breakfast"]),
    ("豆浆", "staple", ["breakfast"]),
    ("芋头饭", "staple", ["breakfast","lunch","dinner"]),
    ("芋头饭（香菇，腊肠，花生，热狗，芋头）", "staple", ["breakfast","lunch","dinner"]),
    ("番薯", "staple", ["breakfast"]),
    ("玉米", "staple", ["breakfast"]),
    ("榨菜", "staple", ["breakfast"]),
    ("豆豉鲮鱼", "staple", ["breakfast"]),
    ("墨鱼饼", "meat", ["lunch","dinner"]),
    ("柠檬鸡爪", "meat", ["lunch","dinner"]),

    # 其他/调味料备注
    ("腊肠", "other", ["lunch","dinner"]),
    ("腊肉", "other", ["lunch","dinner"]),
    ("腊肉腊肠", "other", ["lunch","dinner"]),
    ("瓜咸", "other", ["lunch","dinner"]),
    ("尖椒炒腊肉腊肠", "other", ["lunch","dinner"]),
    ("尖椒炒腊肉", "other", ["lunch","dinner"]),
    ("辣椒炒腊肉", "other", ["lunch","dinner"]),
]

# 去重
seen = set()
dishes = []
for name, cat, meals in ALL:
    if not name or name in seen: continue
    seen.add(name)
    dishes.append({
        "id": f"hist{len(dishes)+1:03d}",
        "name": name,
        "cat": cat,
        "meals": meals,
        "ingredients": "",
        "qty": "",
        "required": False,
        "note": "来自历史菜谱导入",
        "count": 0,
        "source": "历史菜谱导入"
    })

# 按分类排序
order = {"soup":0, "meat":1, "veg":2, "staple":3, "other":4}
dishes.sort(key=lambda x: (order.get(x["cat"], 9), x["name"]))

out = json.dumps(dishes, ensure_ascii=False, indent=2)
print(f"共 {len(dishes)} 道菜品")

with open("/Users/liaoguilong/WorkBuddy/Claw/data/dishes.json", "w", encoding="utf-8") as f:
    f.write(out)

print("已写入 data/dishes.json")
