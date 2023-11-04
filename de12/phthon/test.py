from mt_auto_minhon_mlt import Translator

translator = Translator(
    client_id='9d10c4706d96301a86f80a7794f9b13e06540966d',
    client_secret='634904c2a7859c48abf37bc85bec20cf',
    user_name='hikari00000',
)
en_actual = translator.translate_text('自動翻訳', source_lang='ja', target_lang='en')