set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
" Plugin 'severin-lemaignan/vim-minimap'
Plugin 'severin-lemaignan/vim-minimap'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo

""" I love incsearch, but it was slow when editing rp
" Plugin 'haya14busa/incsearch.vim'
" map /  <Plug>(incsearch-forward)
" map ?  <Plug>(incsearch-backward)
" map g/ <Plug>(incsearch-stay)


Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'christoomey/vim-system-copy'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'tpope/vim-commentary'
Plugin 'mhinz/vim-startify'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" https://github.com/mgedmin/taghelper.vim
Plugin 'mgedmin/taghelper.vim'
set statusline=%<%f\ %h%m%r\ %1*%{taghelper#curtag()}%*%=%-14.(%l,%c%V%)\ %P

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"
"
"
"
"

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set undofile "Persistent undo
set mouse=a
set nu
set paste
set cursorline

"Highlight all search results
set hlsearch

" noremap : ;
noremap ; :

" map [1;5A <C-Up>
" map [1;5B <C-Down>
" map [1;2D <S-Left>
" map [1;2C <S-Right>
" cmap [1;2D <S-Left>
" cmap [1;2C <S-Right>

set smartindent
set tabstop=4
set shiftwidth=4
set expandtab

" Better search highlight color: blue
	"hi Search ctermfg=NONE  ctermbg=blue
	hi Search ctermfg=white  ctermbg=blue

" Some styling; the vertical separators are ugly as hecklestein
	nmap <C-C> cp
" NOTE: To see all available colors, use :help cterm-colors
	set fillchars+=vert:\|
"set fillchars+=vert:\
" set fillchars+=vert:⁞
	hi VertSplit ctermbg=black ctermfg=darkgray
	hi VertSplit ctermbg=darkcyan ctermfg=black
	set fillchars=vert:\|
	hi LineNr ctermfg=darkcyan
	hi LineNr ctermfg=gray
	hi LineNr ctermfg=darkgray
	hi LineNr ctermbg=black
	hi CursorLineNR cterm=bold ctermfg=lightcyan

function ToggleWrap()
 if (&wrap == 1)
   set nowrap
 else
   set wrap
 endif
endfunction
map <F7> :call ToggleWrap()<CR>
map! <F9> ^[:call ToggleWrap()<CR>


"let us toggle paste mode with the shortcut key:
    set pastetoggle=<F2>
    set list "Initially, we're not in list mode, so we <F3
    nmap <F9> : set list! <CR> : hi ryan_tabs ctermfg=DarkGray <CR> : match ryan_tabs /\t/ <CR>
" Let us see tabs and spaces when we're NOT in paste mode...
    set showbreak=↪\ 
    set listchars=tab:▸\ 
    hi ryan_tabs ctermfg=DarkGray
    match ryan_tabs /\t/
" Toggle relative line number
    nmap <F3> : set invrelativenumber <CR>

" Toggle Minimap
    nmap <F4> : MinimapToggle <CR>

" Toggle NERDTree
    nmap <F5> : NERDTreeToggle <CR>

"""""""" The next section: Remeber the cursor position next time we open the same file
" FROM: https://vim.fandom.com/wiki/Restore_cursor_to_file_position_in_previous_editing_session
"               Tell vim to remember certain things when we exit
"                '10  :  marks will be remembered for up to 10 previously edited files
"                "100 :  will save up to 100 lines for each register
"                :20  :  up to 20 lines of command-line history will be remembered
"                %    :  saves and restores the buffer list
"                n... :  where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo
function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction
augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

" Instead of having to type :q! have vim ask us 'Would you like to save? Yes or no'
set confirm
