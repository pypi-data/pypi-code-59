# Imports go here!
from .ahnonlosoio import AhnonlosoioCommand
from .brawlhalla import BrawlhallaCommand
from .cat import CatCommand
from .ciaoruozi import CiaoruoziCommand
from .color import ColorCommand
from .cv import CvCommand
from .cvstats import CvstatsCommand
from .diario import DiarioCommand
from .diarioquote import DiarioquoteCommand
from .diarioshuffle import DiarioshuffleCommand
from .dota import DotaCommand
from .eat import EatCommand
from .elevatormusic import ElevatormusicCommand
from .emojify import EmojifyCommand
from .eval import EvalCommand
from .exec import ExecCommand
from .fortune import FortuneCommand
from .funkwhale import FunkwhaleCommand
from .funkwhalealbum import FunkwhalealbumCommand
from .funkwhaleplaylist import FunkwhaleplaylistCommand
from .givefiorygi import GivefiorygiCommand
from .givetreasure import GivetreasureCommand
from .googlevideo import GooglevideoCommand
from .help import HelpCommand
from .lazyfunkwhale import LazyfunkwhaleCommand
from .lazyfunkwhalealbum import LazyfunkwhalealbumCommand
from .lazyfunkwhaleplaylist import LazyfunkwhaleplaylistCommand
from .lazygooglevideo import LazygooglevideoCommand
from .lazypeertube import LazypeertubeCommand
from .lazyplay import LazyplayCommand
from .lazysoundcloud import LazysoundcloudCommand
from .lazyyahoovideo import LazyyahoovideoCommand
from .lazyyoutube import LazyyoutubeCommand
from .leagueoflegends import LeagueoflegendsCommand
from .magickfiorygi import MagickfiorygiCommand
from .magicktreasure import MagicktreasureCommand
from .matchmaking import MatchmakingCommand
from .pause import PauseCommand
from .peertube import PeertubeCommand
from .peertubeupdates import PeertubeUpdatesCommand
from .ping import PingCommand
from .play import PlayCommand
from .playmode import PlaymodeCommand
from .pmots import PmotsCommand
from .dog import DogCommand
from .queue import QueueCommand
from .rage import RageCommand
from .reminder import ReminderCommand
from .royalpackversion import RoyalpackCommand
from .ship import ShipCommand
from .skip import SkipCommand
from .smecds import SmecdsCommand
from .soundcloud import SoundcloudCommand
from .spell import SpellCommand
from .steammatch import SteammatchCommand
from .steampowered import SteampoweredCommand
from .summon import SummonCommand
from .treasure import TreasureCommand
from .trivia import TriviaCommand
from .userinfo import UserinfoCommand
from .videochannel import VideochannelCommand
from .voicestatus import VoicestatusCommand
from .yahoovideo import YahoovideoCommand
from .youtube import YoutubeCommand

# Enter the commands of your Pack here!
available_commands = [
    AhnonlosoioCommand,
    BrawlhallaCommand,
    CatCommand,
    CiaoruoziCommand,
    ColorCommand,
    CvCommand,
    CvstatsCommand,
    DiarioCommand,
    DiarioquoteCommand,
    DiarioshuffleCommand,
    DotaCommand,
    EatCommand,
    ElevatormusicCommand,
    EmojifyCommand,
    EvalCommand,
    ExecCommand,
    FortuneCommand,
    FunkwhalealbumCommand,
    FunkwhaleCommand,
    FunkwhaleplaylistCommand,
    GivefiorygiCommand,
    GivetreasureCommand,
    GooglevideoCommand,
    HelpCommand,
    LazyfunkwhalealbumCommand,
    LazyfunkwhaleCommand,
    LazyfunkwhaleplaylistCommand,
    LazygooglevideoCommand,
    LazypeertubeCommand,
    LazyplayCommand,
    LazysoundcloudCommand,
    LazyyahoovideoCommand,
    LazyyoutubeCommand,
    LeagueoflegendsCommand,
    MagickfiorygiCommand,
    MagicktreasureCommand,
    MatchmakingCommand,
    PauseCommand,
    PeertubeCommand,
    PeertubeUpdatesCommand,
    PingCommand,
    PlayCommand,
    PlaymodeCommand,
    PmotsCommand,
    DogCommand,
    QueueCommand,
    RageCommand,
    ReminderCommand,
    RoyalpackCommand,
    ShipCommand,
    SkipCommand,
    SmecdsCommand,
    SoundcloudCommand,
    SpellCommand,
    SteammatchCommand,
    SteampoweredCommand,
    SummonCommand,
    TreasureCommand,
    TriviaCommand,
    UserinfoCommand,
    VideochannelCommand,
    VoicestatusCommand,
    YahoovideoCommand,
    YoutubeCommand,
]

# Don't change this, it should automatically generate __all__
__all__ = [command.__name__ for command in available_commands]
