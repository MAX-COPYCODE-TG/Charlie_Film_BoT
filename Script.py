class script(object):
    START_TXT = """𝘏𝘦𝘭𝘭𝘰 {},
𝘔𝘺 𝘕𝘢𝘮𝘦 𝘐𝘴 <a href=https://t.me/{}>{}</a>, 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴, 𝘑𝘶𝘴𝘵 𝘈𝘥𝘥 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘈𝘯𝘥 𝘌𝘯𝘫𝘰𝘺 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ : {}
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/MalluBlasters>Mr KD</a>
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : 𝘏𝘦𝘳𝘰𝘬𝘶
💹 ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 13.0 [ ʙᴇᴛᴀ ]</b>"""
    SETTING_TXT = """<b>ѕeттιngѕ
~ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.
~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

noтe
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

coммand and υѕeѕ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ</a>"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ : <b>ғɪʟᴛᴇʀs</b>
- ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ s_ᴅ_ᴅᴇᴇᴢᴜᴢᴢᴀ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ
<b>ɴᴏᴛᴇ ➾</b>
1. ᴛʜɪs ʙᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.
<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>
‣ /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
‣ /filters - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
‣ /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
‣ /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>
‣ <code>/g_filter</code> ᴏғғ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴏᴀɴᴅ + ᴏɴ/ᴏғғ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴄᴏɴᴛʀᴏʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ"""
    BUTTON_TXT = """ʜᴇʟᴘ : <b>ʙᴜᴛᴛᴏɴs</b>
‣ ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.
<b>ɴᴏᴛᴇ ➾</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴇsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs ➾</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonurl: ᴀɴᴛʀ ʏᴏᴜʀ ʙᴜᴛᴛᴏɴᴜʀʟ)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ➾</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonalert: ᴛʜɪs ɪs ᴀɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ)</code>"""
    AUTOFILTER_TXT = """ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴏɴ/ᴏғғ ᴍᴏᴅᴜʟᴇ
ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
〰〰〰〰〰〰〰〰〰〰〰〰〰
‣ /autofilter ᴏɴ - ᴀᴜᴛᴏғɪʟᴛᴇ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ
‣ /autofilter ᴏғғ - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ
ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴛᴏ ғɪʟᴛᴇʀ ᴀɴᴅ sᴀᴠᴇ ᴛʜᴇ ғɪʟᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴏɴ ᴀɴᴅ ᴏғғ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ..../
ᴄᴏᴍᴍᴀɴᴅs ➾
‣ /set_template - sᴇᴛ ᴄᴜsᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ
‣ /get_template - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ
<b>ᴄʀᴇᴀᴛᴏʀ ➾ </b> <a href=tg://settings><b>ᴛʜɪs ᴘᴇʀsᴏɴ</b></a>
<b>ᴅᴇᴠᴏʟᴏᴘᴇʀ ➾ </b> <a href=https://t.me/MalluBlasters><b>𒆜ᴍʀ ᴋᴅ [ᴏғғɪᴄɪᴀɪʟ] 🇮🇳</b></a>"""
    EXTRAMOD_TXT = """ʜᴇʟᴘ : <b>ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs</b>
<b>ɴᴏᴛᴇ ➾</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴛʜɪs ʙᴏᴛ
<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>
‣ /id - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғᴇᴅ ᴜsᴇʀ.</code>
‣ /info - <code>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.</code>
‣ /imdb - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ.</code>
‣ /search - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇ.</code>"""
    ADMIN_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>
🔋 <u><b>Basic Command</b></u>
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>
🗂️ <u><b>Database & Server Command</b></u>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀᴛʙᴀꜱᴇ ꜱᴛᴀᴛᴜꜱ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>"""
    STATUS_TXT = """<b>╭──᛬⚡️sᴛᴀᴛᴜs ʙᴏᴀʀᴅ⚡️᛬─╮
├╼<b> 📂 ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code></b>
├╼<b> 🌐 ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code></b>
├╼<b> 🔮 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs : <code>{}</code></b>
├╼<b> 💥 ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>
├╼<b> 🎃 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>
╰────────────────╯</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    OWNER_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟</b>
    
<b>• ꜰᴜʟʟ ɴᴀᴍᴇ : 𒆜ᴍʀ ᴋᴅ [ᴏғғɪᴄɪᴀɪʟ] 🇮🇳</b>
<b>• ᴜꜱᴇʀɴᴀᴍᴇ : @MalluBlasters</b>
<b>• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href=https://t.me/MalluBlasters>ᴄʟɪᴄᴋ ʜᴇʀᴇ</b></a>"""
