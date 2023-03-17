# #******************************************************************************#
# # Copyright(c) 2019-2023, Elemento srl, All rights reserved                    #
# # Author: Elemento srl                                                         #
# # Contributors are mentioned in the code where appropriate.                    #
# # Permission to use and modify this software and its documentation strictly    #
# # for personal purposes is hereby granted without fee,                         #
# # provided that the above copyright notice appears in all copies               #
# # and that both the copyright notice and this permission notice appear in the  #
# # supporting documentation.                                                    #
# # Modifications to this work are allowed for personal use.                     #
# # Such modifications have to be licensed under a                               #
# # Creative Commons BY-NC-ND 4.0 International License available at             #
# # http://creativecommons.org/licenses/by-nc-nd/4.0/ and have to be made        #
# # available to the Elemento user community                                     #
# # through the original distribution channels.                                  #
# # The authors make no claims about the suitability                             #
# # of this software for any purpose.                                            #
# # It is provided "as is" without express or implied warranty.                  #
# #******************************************************************************#
#
# #------------------------------------------------------------------------------#
# #Authors:                                                                      #
# #- Gabriele Gaetano Fronze' (gfronze at elemento.cloud)                        #
# #- Filippo Valle (fvalle at elemento.cloud)                                    #
# #------------------------------------------------------------------------------#
#

import regex as re


class usbipyDevice():
    def __init__(self, busid=None, name=None, info=None, id=None, host=None):
        self.busid = self.set_busid(busid) if busid is not None else None
        self.name = name.replace("  ", "")[1:]
        self.info = info
        self.id = id
        self.host = host
        self.port = None

    def set_busid(self, busid: str):
        match = re.search("[0-9]{1,}-[0-9.]{1,}", busid)
        if match:
            return match.group()
        else:
            return None

    def __repr__(self):
        return f"{self.name} {self.info} ({self.busid}) [{self.id}]" + \
            (" "+ self.port if self.port is not None else "")
