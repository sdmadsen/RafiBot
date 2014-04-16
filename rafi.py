from ircBase import *
import modules.imageModule as imageModule
import modules.redditModule as redditModule
import modules.apTrackingModule as apTrackingModule
import modules.fourdeezModule as fourdeezModule
import modules.weatherModule as weatherModule
import modules.smsModule as smsModule
import modules.baseModule as baseModule
import modules.dogecoinModule as dogecoinModule
import modules.errorLoggingModule as errorLoggingModule
import modules.androidServiceModule as androidServiceModule

rafi = IrcBot()
rafi.attachModule(imageModule.ImageModule())
rafi.attachModule(redditModule.RedditModule())
rafi.attachModule(apTrackingModule.ApTrackingModule())
rafi.attachModule(fourdeezModule.FourdeezModule())
rafi.attachModule(weatherModule.WeatherModule())
rafi.attachModule(smsModule.SmsModule())
rafi.attachModule(dogecoinModule.dogecoinModule())
rafi.attachModule(baseModule.BaseModule())
rafi.attachModule(errorLoggingModule.ErrorLoggingModule())
rafi.attachModule(androidServiceModule.AndroidServiceModule())
rafi.run()
