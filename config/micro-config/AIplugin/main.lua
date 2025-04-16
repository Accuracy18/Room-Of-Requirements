local micro = import('micro')
local config = import('micro/config')
local shell = import('micro/shell')
local util = import('micro/util')

function onBufferOpen(bp)
	config.MakeCommand("gemini", Gemini, config.NoComplete)
end

function Gemini(bp, args)
    cursor = bp.Cursor
            
    selection = cursor:GetSelection()

    selection = util.String(selection)

    local prompt = ""
    
    if cursor:HasSelection() then
        prompt = selection
        micro.InfoBar():Message(5)

    else
        prompt = args[1]
        micro.InfoBar():Message(6)
    end
    
	local request = shell.ExecCommand('cgemini', '-r', prompt)

    bp.Buf:Insert(-bp.Cursor.Loc, request)
    
    --micro.InfoBar():Message(selection)
    --bp:InsertNewline()
end
