syntax enable
"重设配色方案"
colorscheme desert
set fencs=utf-8,cp936,gbk
"set spell"
set encoding=utf8
set ffs=unix,dos,mac
set nu
set mouse=a "always use mouse
set lbr
set tw=500
set ai "Autoindent
set si "Smart indent
set wrap "wrap lines
set autoread
filetype plugin on
filetype indent on
set wildmenu   
"增强 模式中的命令自动完成操作"
set cin    
"设置C程序的缩进"
set sw=4	
"设置缩进使用4个空格"
set autoindent
set smartindent 
set tabstop=4
set sta
filetype on  
"检测文件的类型"
set history=1000
set background=dark
set showmatch
set ruler	
"在编辑过程中，在右下角显示光标位置的状态行"
set incsearch
hi Comment ctermfg=DarkCyan
set magic
set showmatch
set lazyredraw
set hlsearch
let mapleader=","
map <silent> <leader>ee :e ~/.vimrc<cr>
let Tlist_Ctags_Cmd='/bin/ctags'  
let Tlist_Show_One_File=1  
let Tlist_Ctags_Cmd="/usr/bin/ctags"
"if &diff
"	let Tlist_Auto_Open=0
"else
"	let Tlist_Auto_Open=1
"endif
let Tlist_Use_Right_Window=1
let Tlist_Exit_OnlyWindow=1  
nmap <F6> :Tlist<CR>
"配置autoinfo的信息，插入作者相应的信息"
let g:vimrc_author='Hunter' 
let g:vimrc_email='tangbao1113@gmail.com' 
let g:vimrc_homepage='http://weibo.com/tonytab' 
nmap <F4> :AuthorInfoDetect<cr>

"配置NERD Tree 文件浏览器"
let NERDTreeWinPos = "right" "where NERD tree window is placed on the screen
let NERDTreeWinSize = 30 "size of the NERD tree
nmap <F7> <ESC>:NERDTreeToggle<RETURN>

"set laststatus=2
"highlight StatusLine cterm=bold ctermfg=yellow ctermbg=blue
" 获取当前路径，将$HOME转化为~
 function! CurDir()
     let curdir = substitute(getcwd(), $HOME, "~", "g")
         return curdir
endfunction
"set statusline=[%n]\ %f%m%r%h\ \|\ \ pwd:\ %{CurDir()}\ \ \|\ %l,%c\ %p%%\ \
"
"
"MiniBufExplorer 配置文件"
let g:miniBufExplMapWindowNavVim=1
let g:miniBufExplMapWindowNavArrows=1
let g:miniBufExplMapCTabSwitchBufs=1
let g:miniBufExplModSelTarget=1


"代码自动补全功能"
set nocp
filetype plugin on
set ofu=syntaxcomplete
let g:pydiction_location='/usr/share/vim/vim73/pydiction/complete-dict'
let g:pydiction_menu_hight=20
autocmd FileType python set omnifunc=pythoncomplete#Complete
"设置python 运行的快捷方式"
nmap <F5> :! python %<cr>
function Addtitle()
	call setline(1, '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">')
	call setline(2,'<html xmlns="http://www.w3.org/1999/xhtml">')
	call setline(3,'<head>')
	call setline(4,'<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>')
	call setline(5,'<title>无标题文档</title>')
	call setline(6,'</head>')
	call setline(9,'</html>')
endfunction
map ml:call Addtitle()<CR>
 "html/xhtml editing in vim (写完>后自动不全结束标签)
  function! InsertHtmlTag()
          let pat = '\c<\w\+\s*\(\s\+\w\+\s*=\s*[''#$;,()."a-z0-9]\+\)*\s*>'
          normal! a>
          let save_cursor = getpos('.')
          let result = matchstr(getline(save_cursor[1]), pat)
          "if (search(pat, 'b', save_cursor[1]) && searchpair('<','','>', 'bn',0,getline('.')) > 0)
          if (search(pat, 'b', save_cursor[1]))
             normal! lyiwf>
               normal! a</
                   normal! p
                      normal! a>
                     endif
                      :call cursor(save_cursor[1], save_cursor[2], save_cursor[3])
          endfunction
          inoremap > <ESC>:call InsertHtmlTag()<CR>a
