import menu_bot as menu
import sql
import states as state
import text


def side_job(update, _):
    update.message.reply_markdown(text=text.SIDE_JOB_DESC, reply_markup=menu.show(menu=text.SIDE_JOB))
    return state.SIDE_JOB


def invite(update, _):
    update.message.reply_markdown(text=text.REFERRAL_LINK.format(id=update.message.chat.id))
    update.message.reply_markdown(text=text.INVITE_DESC, reply_markup=menu.show(menu=text.PAYMENT))
    return state.INVITE


def invite_payment(update, _):
    referrals = sql.get_completed_referrals(referrer=update.message.chat.id)
    if not referrals:
        update.message.reply_markdown(
            text=text.NO_COMPLETED_REFERRALS, reply_markup=menu.show(menu=text.PAYMENT)
        )
    else:
        for (ref_id, ref_nick) in referrals:
            sql.add_completed_referral(referrer=update.message.chat.id, referral=ref_id)
            update.message.reply_markdown(
                text=text.SUCCESSFUL_REFERRAL.format(nick=ref_nick), reply_markup=menu.show(menu=text.PAYMENT)
                                          )
        return state.INVITE
