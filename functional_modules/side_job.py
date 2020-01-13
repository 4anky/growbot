import config
import menu_bot as menu
import sql
import states as state


def side_job(update, _):
    update.message.reply_markdown(text=config.SIDE_JOB_DESC, reply_markup=menu.show(menu=config.SIDE_JOB))
    return state.SIDE_JOB


def invite(update, _):
    update.message.reply_markdown(text=config.REFERRAL_LINK.format(id=update.message.chat.id))
    update.message.reply_markdown(text=config.INVITE_DESC, reply_markup=menu.show(menu=config.PAYMENT))
    return state.INVITE


def invite_payment(update, _):
    referrals = sql.get_completed_referrals(db_path=config.DB_PATH, referrer=update.message.chat.id)
    if not referrals:
        update.message.reply_markdown(
            text=config.NO_COMPLETED_REFERRALS, reply_markup=menu.show(menu=config.PAYMENT)
        )
    else:
        for (ref_id, ref_nick) in referrals:
            sql.add_completed_referral(
                db_path=config.DB_PATH, referrer=update.message.chat.id, referral=ref_id
            )
            update.message.reply_markdown(
                text=config.SUCCESSFUL_REFERRAL.format(nick=ref_nick), reply_markup=menu.show(menu=config.PAYMENT)
                                          )
        return state.INVITE
