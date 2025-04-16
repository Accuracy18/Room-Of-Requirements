local micro = import('micro')
local config = import('micro/config')
local shell = import('micro/shell')

function onBufferOpen(bp)
	config.MakeCommand("template", Template, config.NoComplete)
end

function Template(bp, args)
    local commandArgs = {}
    
	local request = shell.ExecCommand('template_generate', '-f', args[1])
    bp.Buf:Insert(-bp.Cursor.Loc, request)

    --bp:InsertNewline()
    --micro.InfoBar():Message(args[1])
end
