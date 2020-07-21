import requests
import json
import uuid
import base64
from urllib.parse import urljoin
from pathlib import Path
import os
import re
from xml.dom import minidom
from string import Template, Formatter
from robot.api.deco import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from .version import __VERSION__

cwdPath = Path.cwd()
thisPath = Path(__file__).parent

class ATPKeywords(object):
    """
    ATP Keywords Library for RobotFramework
    """
    
    ROBOT_LIBRARY_SCOPE = 'Global'
    ROBOT_LIBRARY_VERSION = __VERSION__

    ATP_DEFAULT_IMAGEPROCESSOR = 'local'
    ATP_DEFAULT_ATPURL = 'http://localhost:9090/'
    ATP_DEFAULT_RELAYATPURL = 'http://localhost:9090/'
    ATP_DEFAULT_KEYMAP = "USKeyboard"

    def __init__(self, atpUrl=ATP_DEFAULT_ATPURL, imageProcessor=ATP_DEFAULT_IMAGEPROCESSOR, relayAtpUrl=ATP_DEFAULT_RELAYATPURL, keyMap=ATP_DEFAULT_KEYMAP, keyMapPath=None):

        self._atpUrl = atpUrl
        self._imageProcessor = imageProcessor
        self._relayAtpUrl = relayAtpUrl
        self._keyMapName = keyMap
        self.builtin = BuiltIn()

        try:
            #use internal keymappings
            if keyMapPath is None:
                self._keyMapDoc = minidom.parse(str(thisPath.joinpath("KeyMappings.xml")))
            else:
                if os.path.isabs(keyMapPath):
                    self._keyMapDoc = minidom.parse(keyMapPath)
                else:
                    self._keyMapDoc = minidom.parse(str(cwdPath.joinpath(keyMapPath)))

            self._keyMap = self._getKeyMapping(self._keyMapName)

            pingResponse = self._call(self._getAtpUrl('v3'), 'performPing')
            if pingResponse is None or pingResponse['Successful'] == False:
                raise RuntimeError('Unable to ping ATP instance at ' + self._atpUrl)

            if self._imageProcessor == 'relay':
                if self._relayAtpUrl is None:
                    raise RuntimeError('Invalid ATP relay url provide: ' + self._relayAtpUrl)
                pingResponse = self._call(self._getRelayAtpUrl('v3'), 'performPing')
                if pingResponse is None or pingResponse['Successful'] == False:
                    raise RuntimeError('Unable to ping ATP relay instance: ' + self._relayAtpUrl)

            # if self._keyMap is not None:
            #     keyMapResponse = self._call(self._getAtpUrl('v2'), 'setKeyMappings', [self._keyMap])
            #     if keyMapResponse['Successful'] == False:
            #         raise Exception('Unable to set ATP KeyMapping!')
        except Exception as error:
            raise RuntimeError('Unable to initialize ATPLibrary: ' + str(error))

    # Gets the ATP Url endpoint based on version (default v3)
    def _getAtpUrl(self, version='v3'):
        return urljoin(self._atpUrl, 'ATP/' + version)

    # Gets the ATP Relay Url endpoint based on version (default v3)
    def _getRelayAtpUrl(self, version='v3'):
        return urljoin(self._relayAtpUrl, 'ATP/' + version)

    # Gets KeyMapping by name
    def _getKeyMapping(self, name):
        items = self._keyMapDoc.getElementsByTagName('KeyMapping')
        i = None
        for item in items:
            if item.attributes['name'].value == self._keyMapName:
                i = item
                break

        keyMapping = None

        if i is not None:
            keyMapping = {
                "keyMappings": []
            }

            keys = i.getElementsByTagName('Key')
            for key in keys:
                keyMapping['keyMappings'].append({ 
                    "id": key.attributes['id'].value,
                    "keyCode": key.attributes['keycode'].value,
                    "name": key.attributes['name'].value
                })

        return keyMapping

    # Gets Key from set KeyMapping by name
    def _getKeyByName(self, name):
        for key in self._keyMap['keyMappings']:
            if key['name'] == name:
                return key
        return None

    # Gets Key from set KeyMapping by id
    def _getKeyById(self, id):
        for key in self._keyMap['keyMappings']:
            if key['id'] == id:
                return key
        return None

    # Gets Key from set KeyMapping by keyCode
    def _getKeyByCode(self, code):
        for key in self._keyMap['keyMappings']:
            if key['keyCode'] == code:
                return key
        return None

    # Creates a KeyAction (used within a KeySequence) from a Key object
    def _createKeyAction(self, key, press=True, release=True, preDelay=0, postDelay=0):
        return {
            "key": key,
            "press": press,
            "release": release,
            "preDelay": preDelay,
            "postDelay": postDelay,
            "returnScreenBuffer": False
        }

    # Gets a KeySequence (list of KeyActions) from a string. This decodes Tokens '{}' as Keys from Key Mapping
    # Otherwise decodes each character within string as a key.
    def _getKeySequenceFromString(self, keys):
        keySeq = []
        tokens = [el[1] for el in Formatter().parse(keys) if el[1] is not None]
        
        inToken = False
        tokenAdded = False

        for i in range(len(keys)):
            c = keys[i]

            #Start of a token
            if not inToken and c == "{":
                inToken = True
                tokenAdded = False

                for token in tokens:
                    if keys[i+1:i+1+len(token)] == token:
                        tokenItems = token.split('+')
                        tokenSeq = []

                        for t in range(len(tokenItems)):
                            tokenItem = tokenItems[t]
                            lastTokenItem = t == len(tokenItems)-1
                            tokenSuffixLen = 0
                            release = True

                            if not lastTokenItem:
                                tokenSuffixLen = 1
                                release = False

                            k = self._getKeyByName(tokenItem)
                            if k is not None:
                                keySeq.append(self._createKeyAction(k, release=release))
                                tokenAdded=True
                                i+=len(tokenItem) + tokenSuffixLen
                            else:
                                k = self._getKeyByCode(tokenItem)
                                if k is not None:
                                    keySeq.append(self._createKeyAction(k, release=release))
                                    tokenAdded=True
                                    i+=len(tokenItem) + tokenSuffixLen
                                else:
                                    k = self._getKeyById(tokenItem)
                                    if k is not None:
                                        keySeq.append(self._createKeyAction(k, release=release))
                                        tokenAdded=True
                                        i+=len(tokenItem) + tokenSuffixLen

                            if k is not None and not lastTokenItem:
                                tokenSeq.append(k)

                        if len(tokenSeq) > 0:
                            tokenSeq.reverse()
                            for k in tokenSeq:
                                keySeq.append(self._createKeyAction(k, press=False, release=True))

            if inToken and c == "}":
                inToken = False
                tokenAdded = False
            elif not tokenAdded:
                k = self._getKeyByName(c)
                if k is not None:
                    keySeq.append(self._createKeyAction(k))

        return keySeq


    # Validates an ATPResponse object.
    # If result = True - Validate a 'result' object was returned in the ATP Response, and that response was successful
    # If errors = True - Validate response does not have errors reported aswell
    def _validateResponse(self, response, result=True, errors=True):
        try:
            logger.debug('ATP:validateResponse')
            logger.debug(json.dumps(response, indent=4))

            if result == True:
                if response['result']:
                    assert response['result'], 'Invalid ATP Response'
                    assert response['result']['Successful'] == True, 'ATP Response was not successful'
                    #assert response['result']['Result'], 'ATP Response has no result'
                    if errors == True:
                        assert len(response['result']['Errors']) == 0, 'ATP Response contains errors'
                else:
                    assert response != None, 'Invalid ATP Response'
            if response['result']:        
                return response['result']
            else:
                return response
        except Exception as error:
            raise RuntimeError('Invalid ATP Response: ' + str(error))

    # Performs an ATP Call using HTTP Post against ATP Server, via a JSON RPC payload.
    def _call(self, url, method, params=[{}], validateResult=True, validateErrors=True):
        try:
            logger.debug('ATP:call ' + method + ' @ ' + url)

            payload = {
                "method": method,
                "params": params,
                "jsonrpc": "2.0",
                "id": str(uuid.uuid4())
            }

            response = requests.post(url, json=payload)

            logger.debug(response.text)
            
            return self._validateResponse(response.json(), validateResult, validateErrors)
        except Exception as error:
            raise RuntimeError('ATP Request error: ' + str(error))

    # Reads a local image file, and returns as a Base64 String. (To be used when sending within ATP Requests)
    def _read_image(self, filename):
        filepath = self._parse_filepath(filename)

        with open(filepath.absolute(), "rb") as imgFile:
            imgBytes = imgFile.read()

        base64Bytes = base64.b64encode(imgBytes).decode('utf-8')
        return str(base64Bytes)

    # Parses a filename string. Either will check if absolute and exists, otherwise
    # resolves based on Command Working Directory and returns the absolute path
    def _parse_filepath(self, filepath):
        filepath = Path(filepath)
        if not filepath.is_absolute() and not filepath.exists():
            filepath = cwdPath.joinpath(filepath)
        return filepath.absolute()


    # Checks if a string is base64 encoded.
    def _is_base64(self, s):
        pattern = re.compile("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$")
        if not s or len(s) < 1:
            return False
        else:
            return pattern.match(s)

    # Calls the ATP Ping method. Used to ping the ATP Server
    @keyword("ATP Ping")
    def atp_ping(self):
        """ ATP Ping: Pings ATP server """
        return self._call(self._getAtpUrl('v3'), 'performPing',[{}], True)

    # Calls the ATP Kill method. Kills the remote ATP Server process
    @keyword("ATP Kill")
    def atp_kill(self):
        """ ATP Kill: Kills ATP server """
        return self._call(self._getAtpUrl('v2'), 'kill', [], False)

    # Calls the ATP Delay method. Performs a Thread delay with the ATP server process.
    @keyword("ATP Delay")
    def atp_delay(self, duration):
        """ ATP Delay: Delays X milliseconds
        @duration: duration to delay for in milliseconds """
        return self._call(self._getAtpUrl('v2'), 'delay', [duration], False)

    # Calls the ATP Take Screen Capture method. Takes a remote screen shot of the machine running 
    # the ATP Server component, and returns image (PNG) as a Base64 String
    @keyword("ATP Take Screen Capture")
    def atp_take_screen_capture(self):
        """ ATP Take Screen Capture: Takes Screen capture on ATP server """
        return self._call(self._getAtpUrl('v2'), 'takeScreenCapture',[], True)

    # Calls the ATP Take Screen Capture method and saves to local file. Takes Screen Shot on remote ATP server
    # and saves to local file
    @keyword("ATP Save Screen Capture")
    def atp_save_screen_capture(self, filename):
        """ ATP Save Screen Capture: Takes and Saves screen capture from ATP server to file 
        @filename: filename where to save screen capture to as png file """
        response = self.atp_take_screen_capture()
        data = base64.b64decode(response['Result'])
        with open(filename, 'wb') as f:
            f.write(data)

    # Calls the ATP Find Image In method. Uses a ATP Server to find a image within another image.
    # This is normally used within a Relay setup, where host does not support Sikuli, and hence takes
    # screen shot, and uses another host to perform find image in, to get results (location of image) within
    # other image.
    @keyword("ATP Find Image In")
    def atp_find_image_in(self, findImage, targetImage, findText=None, tolerance=0.95):
        """ ATP Find Image In: Finds image inside another image 
        @findImage: Serializable Image to find within 'targetImage'
        @targetImage: Serializable Image used to find 'findImage' within
        @findText: Text to find within 'targetImage' default = None
        @tolerance: Tolerance level between 0 and 1. default = 0.95"""
        findInPayload = {
            "tolerance": tolerance,
            "findText": findText,
            "findImage": findImage,
            "targetImage": targetImage
        }

        if self._imageProcessor == 'relay':
            return self._call(self._getRelayAtpUrl('v3'), 'performFindImageIn',[findInPayload], True)
        else:
            return self._call(self._getAtpUrl('v3'), 'performFindImageIn', [findInPayload], True)

    # Calls the ATP Click method. Used to perform a mouse click based on:
    # Image location
    # Offset (either offset of entire screen, when no image defined, or offset from where the image was found)
    @keyword("ATP Click")
    def atp_click(self, type='LEFTSINGLE', image=None, offset=None, highlight=False, preDelay=0, postDelay=0, tolerance=0.95):
        """ ATP Click: Mouse moves and clicks where an image is found 
        @type: Type of click to perform default = 'LEFTSINGLE' ['LEFTSINGLE', 'MIDDLESINGLE', 'RIGHTSINGLE', 'LEFTDOUBLE', 'MIDDLEDOUBLE', 'RIGHTDOUBLE']
        @image: Image used to find location where to perform click. (Serializable Image or a File path to image to find) default = None
        @offset: 'X,Y' or positive / negative integer to offset from the found location. default = None. eg: 200,150 / -100,-20 / 2*,2* (Half width, half height)
        @highlight: True to highlight location found before clicking. default = False
        @preDelay: No of milliseconds to delay before click. default = 0
        @postDelay: No of milliseconds to delay after click. default = 0
        @tolerance: Tollerance for 'image' found between 0 and 1. default = 0.95 """
        calcOffset = None
        clickPayload = {
            "clickType": type,
            "highlight": highlight,
            "preDelay": preDelay,
            "postDelay": postDelay
        }

        if image is not None:
            if self._imageProcessor == "relay":
                
                imageData = self._read_image(image)
                logger.debug('Find: ' + imageData)

                findImage = {
                    "imageData": imageData,
                    "imagePath": image
                }

                targetResponse = self.atp_take_screen_capture()
                logger.debug('Target: ' + targetResponse['Result'])

                targetImage = {
                    "imageData": targetResponse['Result']
                }

                findImageInResponse = self.atp_find_image_in(findImage, targetImage, tolerance=tolerance)

                #need to validate response matches
                match = findImageInResponse['Result']['Matches'][0]

                if offset is not None:
                    #Offset the found image location
                    offsetSplit = offset.split(",")
                    offsetX = offsetSplit[0].trim()
                    offsetY = offsetSplit[1].trim()
                    calcOffset = str(match['x'] + int(offsetX)) + ',' + str(match['y'] + int(offsetY))
                else:
                    #Calc middle of found region
                    calcOffset = str(match['x'] + int(match['width'] / 2)) + ',' + str(match['y'] + int(match['height'] / 2))

            else:
                if self._is_base64(image):
                    clickPayload['image'] = {
                        "imageData": image
                    }
                else:
                    clickPayload['image'] = {
                        "imageData": self._read_image(image),
                        "imagePath": image
                    }

                calcOffset = offset
        else:
            calcOffset = offset
            
        clickPayload['clickOffset'] = calcOffset
        
        clickResponse = self._call(self._getAtpUrl('v3'), 'performClick', [clickPayload], True)
        
        return clickResponse

    # Calls the ATP KeyPress method. Performs a single KeyAction (with press = True) based on a Key element
    @keyword("ATP Key Press")
    def atp_keyPress(self, key, release=True, preDelay=0, postDelay=0):
        """ ATP KeyPress: Press a single key (default to not release)
        @key: KeyCode (object) to press
        @release: Release Key. default = True
        @preDelay: No of milliseconds to delay before pressing key. default = 0
        @postDelay: No of milliseconds to delay after pressing key. default = 0 """
        if isinstance(key, str):
            key = self._getKeySequenceFromString(key)
            if len(key) != 1:
                raise Exception('Inavlid key value specified for keyPress!')

        payload = {
            "key": key[0],
            "press": True,
            "release": release,
            "preDelay": preDelay,
            "postDelay": postDelay,
            "returnScreenBuffer": False
        }
        
        response = self._call(self._getAtpUrl('v3'), 'keyPress', [payload], True)
        
        return response

    # Calls the ATP KeyRelease method. Performs a single KeyAction (with press = False, Release = True) based on a Key element
    @keyword("ATP Key Release")
    def atp_keyRelease(self, key, preDelay=0, postDelay=0):
        """ ATP KeyRelease: Release previously pressed key
        @key: KeyCode (object) to press
        @preDelay: No of milliseconds to delay before releasing key. default = 0
        @postDelay: No of milliseconds to delay after releasing key. default = 0  """
        if isinstance(key, str):
            key = self._getKeySequenceFromString(key)
            if len(key) != 1:
                raise Exception('Inavlid key value specified for keyPress!')

        payload = {
            "key": key[0],
            "press": False,
            "release": True,
            "preDelay": preDelay,
            "postDelay": postDelay,
            "returnScreenBuffer": False
        }
        
        response = self._call(self._getAtpUrl('v3'), 'keyRelease', [payload], True)

        return response

    # Calls the ATP KeyPress Sequence method. This takes in a string and decodes this into a key sequence (collection of Key Actions)
    # String is decoded by tokens {..} that if match a Key within the current Key Mapping, otherwise decodes each character within the string
    @keyword("ATP Press")
    def atp_keyPressSequence(self, keys, preDelay=0, postDelay=0):
        """ ATP KeyPressSequence: Press and release numerious keys
        @keys: String sequence of keys to press. Tokens '{}' define a named key from Key Mapping. Key tokens can contain key combinations eg: {Windows+r} to press Windows key and 'r' at the same time
        @preDelay: No of milliseconds to delay before pressing each key in sequence. default = 0
        @postDelay: No of milliseconds to delay after pressing each key in sequence. default = 0  """
        if isinstance(keys, str):
            keys = self._getKeySequenceFromString(keys)

        payload = {
            "sequence": keys,
            "preDelay": preDelay,
            "postDelay": postDelay,
            "detectScreenChange": False,
            "screenChangeTimeout": 30000,
            "screenChangeArea": "0,0,*,*",
            "actionDelay": 250,
            "returnScreenBuffer": False
        }
        
        response = self._call(self._getAtpUrl('v3'), 'keyPressSequence', [payload], True)
        
        return response

    @keyword("ATP Get Settings")
    def atp_getSettings(self):
        """ ATP Get Settings: Retrieves Proxy Settings from ATP Server """
        return self._call(self._getAtpUrl('v2'), 'getSettings',[], True)

    @keyword("ATP Set Settings")
    def atp_setSettings(self, settings):
        """ ATP Set Settings: Sets Proxy Settings for ATP Server
        @settings: Collection of Setting objects to set on ATP server instance """
        return self._call(self._getAtpUrl('v2'), 'setSettings',[settings], True)

    @keyword("ATP Open App")
    def atp_openApp(self, command):
        """ ATP Open App: Sends command to open application using Sikuli
        @command: Command string passed to Sikuli openApp """
        payload = {
            "command": command,
        }

        return self._call(self._getAtpUrl('v3'), 'performOpenApp', [payload], True)

    @keyword("ATP Close App")
    def atp_closeApp(self, appName):
        """ ATP Open App: Sends command to open application using Sikuli
        @appName: Name of the application opened via openApp to be closed. """
        payload = {
            "appName": appName,
        }

        return self._call(self._getAtpUrl('v3'), 'performCloseApp', [payload], True)

    # Calls the ATP Assert method. Validates image exists on the screen
    # type = 'SCREENIMAGE' (default) | 'SCREENTEXT'
    # image = Base64 String of image | Path to image file
    # relative = **Not implemented yet
    # relativeLength = **Not implemented yet
    # tolerance = Tolerance level for asserted (found) image (default 0.95)
    # timeout = Timeout to wait for image to be asserted (default 20000 ms)
    @keyword("ATP Assert")
    def atp_assert(self, image, type="SCREENIMAGE", relative=None, relativeLength=0, tolerance=0.95, timeout=20000):
        """ ATP Assert: Performs an image assert on the remote ATP Server
        @image: Image to assert of screen. Image can be Serializable Image object, or a base64 String of png image file.
        @type: Type of assert to perform ['SCREENIMAGE', 'SCREENTEXT'] default = 'SCREENIMAGE'
        @relative: Not implemented yet
        @relativeLength: Not implemented yet
        @tolerance: Tollerance for 'image' found between 0 and 1. default = 0.95
        @timeout: No of milliseconds to wait to assert """
        payload = {
            "assertType": type,
            "tolerance": tolerance,
            "timeout": timeout,
            "relative": relative,
            "relativeLength": relativeLength
        }

        if self._is_base64(image):
            payload['image'] = {
                "imageData": image
            }
        else:
            payload['image'] = {
                "imageData": self._read_image(image),
                "imagePath": image
            }
            
        return self._call(self._getAtpUrl('v3'), 'performAssert', [payload], True)

    # Calls the ATP Wait Until method. Waits until text or image, appears or vanishes.
    # image = | Base64 String of Image | path to image file
    # text = Text to be detected or vanish (depends on type)
    # textRegEx = True if text is a regular expression, default = False
    # type = 'IMAGEAPPEARS' | 'IMAGEVANISHES' (when image property providedd) | 'TEXTAPPEARS' | 'TEXTVANISHES' (when text property provided)
    # region = 'SCREEN' (default) to use screen to detect | 'WINDOW' to use open application (when open app method call) as detection region
    @keyword("ATP Wait Until")
    def atp_waitUntil(self, image=None, text=None, textRegEx=False, type="IMAGEAPPEARS", region="SCREEN", tolerance=0.95, timeout=30000):
        """ ATP Wait Until: Waits until 'IMAGEAPPEARS', 'IMAGEVANISHES', 'TEXTAPPEARS' or 'TEXTVANISHES'
        @image: Image to wait until. Image can be Serializable Image object, or a base64 String of png image file. default = None
        @text: Text to wait until. Sikuli Text detection is used. default = None
        @textRegEx: True to evaluate 'text' as a regular expression. defaut = False
        @type: Type of wait to occur. ['IMAGEAPPEARS', 'IMAGEVANISHES', 'TEXTAPPEARS', 'TEXTVANISHES'] default = 'IMAGEAPPEARS'
        @region: Region used when waiting for image or text. ['SCREEN', 'WINDOW'] default = 'SCREEN'
        @tolerance: Tollerance for 'image' found between 0 and 1. default = 0.95
        @timeout: No of milliseconds to wait until. default = 30000  """
        payload = {
            "timeout": timeout,
            "tolerance": tolerance,
            "waitUntilType": type,
            "waitUntilRegion": region
        }

        if image is not None:
            if self._is_base64(image):
                payload['image'] = {
                    "imageData": image
                }
            else:
                payload['image'] = {
                    "imageData": self._read_image(image),
                    "imagePath": image
                }
        elif text is not None:
            payload['text'] = text
            payload['textIsRegEx'] = textRegEx

        return self._call(self._getAtpUrl('v3'), 'performWaitUntil', [payload], True)
            
