
# nonviolent_sound_amplifying_WAV_PY
# Smart Nonviolent Audio Sound Amplifier

### It is amplifying audio but not those loud parts.

#### First you define threshold levell ⠀—⠀ saying which parts are to loud. <br> Audio reaching above that level will be amplified just to the ceiling (maximum capacity of 16-bit depth audio) or to the level that user set. <br> Audio quieter than that level will be amplified in a normal way proportionally. <br> <br> <br> By firstly reducing amplitude ⠀of wave bumps ⠀that are prone to be flattened by the ceiling ⠀it surf them from it being distorted. ⠀This makes the silent parts of sound similar in loudness to the louder parts. ⠀And then increasing volume can be done equally for all audio safely.


#### <br> Those pictures show first stage (amplitude reduction) with the same input file and different threshold specified⠀—⠀respectively⠀20 000⠀and⠀10 000.

<img    src="200506śro1618 10_000 + 20_000 .wav mod .png"   >




<br> <br> <br> 

### How to use it:   
#### You just need ` nonviolent_sound_ampl...*.py ` ⠀and ⠀file the ` *.wav. ` file. ⠀The program/script from ` *.py ` will use data from ` *.wav `. ⠀It will create another moddified file.   <br> <br>If you uncomment some parts of the code like ` # plt.savefig() ` you will need other  ` *.py ` files located in this repo.




<br> <br> <br> 

#### If docstring below is not readable please scroll down for pictured version of it.
``` python
it_is_amplifying_audio_but_not_those_loud_parts = """



it change this:

························································································································

                                                                                             ## ####                    
                              #                                                           ###  #   ##                   
                            ####                                                         #          #                   
                          ####  #                                                       ##          ##                  
    ###                   #     ##                                               ##    ##            #                  
   ## #                  #       #                                            # ## #####             ##                 
···#··##·················#·······##·············T·H·R·E·S·H·O·L·D············###······················#·················
  ##   ##               #         #                                          #                        #                 
 ##     ###             #          #                                        ##                        ##                
 #       ###   ##      ##          ##                  ####                 #                          #                
#··········##·###·····##············##················#···##···············##··························#####············
#            ## ##  ###              #              ###    ##       ##     #                                ###   ####  
                 # #                 ##            ##        #  #######  ##                                    ###   #  
                 ###                  ####         #         ####     ####                                            # 
··················#·······················#·······##································T·H·R·E·S·H·O·L·D··················#
                                          ##      #                                                                     
                                           #     ##                                                                     
                                           #   ###                                                                      
                                            # ###                                                                       
                                            ###                                                                         
                                            #                                                                           

························································································································



by this:

························································································································

                                                                                             ·· ····                    
                              ·                                                           ···  ·   ··                   
                            ····                                                         ·          ·                   
                          ····  ·                                                       ··          ··                  
    ···                   ·     ··                                               ··    ··            ·                  
   ·· ·                  ·       ·                                            · ·· ·····             ··                 
·····#························##·····························································#######····················
  ·## #··               · ####  ##·                                          ·           ###        ##·                 
 ··#   ##··             ·#       ##·                                        ··###########            ##·                
 ##     ###·   ##      ·#         ##·                  ####                 ·#                        ##                
##·········##·###·····##············##···············##···##···············##··························#####············
#            ## ##  ###              #####         ##··    ##       ##     #                                ###   ####  
                 # #                 ··   ##      #··        #  #######  ##                                    ###   #  
                 ###                  ···· ## #### ·         ####     ####                                            # 
··················#·························###········································································#
                                          ··      ·                                                                     
                                           ·     ··                                                                     
                                           ·   ···                                                                      
                                            · ···                                                                       
                                            ···                                                                         
                                            ·                                                                           

························································································································



into this:

·····#························##··································································##····················
    ###                     ####                                                            ########                    
    # #                    ### ##                                                        ####      ##                   
   ## #                   ###   #                                                        #          #                   
   #  ##                 ##     ##                                                      ##          ##                  
   #   #                 ##      #                                               ##    ##            #                  
   #   #                 #       #                                              ## #####             ##                 
  ##   ##               ##       ##                     #                     ###                     #                 
··#·····##··············#·········#····················##····················##·······················#·················
 ##      ##    ##       #          #                   ####                  #                        ##                
 #        #    ##      ##          #                  ##  #                 ##                        ##                
##        ##  ###      #           ##                 #   #                 #                          #                
#··········#··#·#·····##············##················#····#···············##··························##···············
#          #### #    ###             #               ##    #               #                             ###            
#            ## #   ###              #             ###     #               #                                #       #   
             #  #   ###               #            #       ##       ##     #                                 ##   ###   
················##·##·················#####········#········#·······##····##··································#··##·##··
                 # ##                     #       ##        ##   #  ##    #                                   ####   #  
                 # #                      ##      #          #  #### ##  ##                                    ##    #  
                 ###                      ##     ##          #  #     #  ##                                          #  
                 ###                       #     #           ## #     # ##                                           ## 
                 ###                       ##  ###            ###     ###                                             # 
                 ##                         # ###             ##                                                      ##
                  #                         ###                                                                       ##
············································##··········································································



avoiding that:

···#####·················#########···········LIMIT·OF·int16·CAPACITY··········#########################·········+32767··
   #···#                ##  ···· ##                                          ##             ········  #                 
   #· ·#                #  ··· ·· #                                          #           ····      ·· #                 
  ##· ·#                # ···   · #                                          #           ·          · #                 
  ##  ·##               #··     ··#                                          #          ··          ··#                 
  #·   ·##              #··      ·##                                         #   ··    ··            ·##                
 ##·   ·###             #·       · #                                        ##  ·· ·····             ·##                
 ##·   ··##             #·       ··#                    #                   ##···                     ·#                
·#·······##·············#··········#···················##···················#··························#················
 #·      ·#    ##      ##          #                   ####                 #·                        ·#                
##        ##   ##      #·          ·#                 ##  #                 #·                        ·#                
#·        ·#  ###      #           ·#                 #   #                 #                          #                
#··········#··#·#·····##············#·················#····#···············##···························#···············
#          #### #    ###            ##               ·#    #               #                             ###            
#            ## #   ###             ##             ··##    #               #                                #       #   
             #  #   ###              #·            · #     ##       ##     #                                 ##   ###   
················##·##················#··············##······#·······##····##··································#··##·##··
                 # #·                #    ·       ·##       ##   #  ##    #                                   ####   #  
                 # #                 ##   ··      ·#         #  #### ##  ##                                    ##    #  
                 ###                  #   ··     ··#         #  #     #  ##                                          #  
                 ###                  #    ·     · #         ## #     # ##                                           ## 
                 ###                  #  # ··  ··· #          #·#     ###                                             # 
                 ##                   ##### · ··· ##          ##                                                      ##
                  #                      ## ···   ##                                                                  ##
··········································##########·························or·some·other·(·like·int16·)··· -32768·····



Works on 16-bit depth wave.
If You want it on other depth   change   new_range_for_amplify   to your max bit capacity.

Activate prints to se the process
and / or
plt.show()

NOTE: Try it on small audio or big computer! ;) """
```



<br> <br> <br> <br> 
## TODO: resign from list of all bumps since idea of usin that list was abandoned.
## TODO: reading file from dysk in chunks so it can works on multihours recordings.




<br> <br> <br> 
<br> <br> <br> <br> <br> <br> 
<img    src="220314pon1803 (PiDayΠπDay) na(((200505wto1228))) wav [ [], [], [], [] ] .py  DocString_jedynie 10 .ods .html x1,7 .png .xcf .png"        >




<br> <br> <br> <br> <br> <br> 
<br> <br> <br> <br> <br> <br> 
<br> <br> <br> <br> <br> <br> 
## And if you want to see it once again:
<img    src="220314pon1803 (PiDayΠπDay) na(((200505wto1228))) wav [ [], [], [], [] ] .py  DocString_jedynie 10 kostki .ods BiałeWszystkieLiterki .html .png .xcf CyanMagenta .jpg"        >