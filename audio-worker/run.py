from gradio_client import Client, handle_file

client = Client("http://127.0.0.1:7865/")
result = client.predict(
    format="wav",
    audio_duration=-1,
    prompt="funk, pop, soul, rock, melodic, guitar, drums, bass, keyboard, percussion, 105 BPM, energetic, upbeat, groovy, vibrant, dynamic",
    lyrics="""[verse]
Neon lights they flicker bright
City hums in dead of night
Rhythms pulse through concrete veins
Lost in echoes of refrains

[verse]
Bassline groovin' in my chest
Heartbeats match the city's zest
Electric whispers fill the air
Synthesized dreams everywhere

[chorus]
Turn it up and let it flow
Feel the fire let it grow
In this rhythm we belong
Hear the night sing out our song

[verse]
Guitar strings they start to weep
Wake the soul from silent sleep
Every note a story told
In this night we’re bold and gold

[bridge]
Voices blend in harmony
Lost in pure cacophony
Timeless echoes timeless cries
Soulful shouts beneath the skies

[verse]
Keyboard dances on the keys
Melodies on evening breeze
Catch the tune and hold it tight
In this moment we take flight
""",
    infer_step=60,
    guidance_scale=15,
    scheduler_type="euler",
    cfg_type="apg",
    omega_scale=10,
    manual_seeds=None,
    guidance_interval=0.5,
    guidance_interval_decay=0,
    min_guidance_scale=3,
    use_erg_tag=True,
    use_erg_lyric=False,
    use_erg_diffusion=True,
    oss_steps=None,
    guidance_scale_text=0,
    guidance_scale_lyric=0,
    audio2audio_enable=False,
    ref_audio_strength=0.5,
    ref_audio_input=None,
    lora_name_or_path="none",
    lora_weight=1,
    api_name="/__call__",
)
print(result)
